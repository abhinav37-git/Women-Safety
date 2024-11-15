import streamlit as st
import speech_recognition as sr
from transformers import AutoModelForCausalLM, AutoTokenizer
from gtts import gTTS
import os
import torch
import playsound
from tempfile import NamedTemporaryFile
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import json

# Load a pre-trained DialoGPT model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Initialize Firebase if not already initialized
with open('config.json') as config_file:
    config = json.load(config_file)

if not firebase_admin._apps:
    cred = credentials.Certificate(config['firebase_credentials'])
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Initialize chat history to maintain conversation context
chat_history_ids = None  # Initialize globally

# Retrieve user data from Firestore
def get_user_data(user_id):
    user_ref = db.collection("User-Collection").document(user_id)
    user_data = user_ref.get().to_dict() if user_ref.get().exists else None
    return user_data


# Function to generate Google Maps URL for current location
def generate_location_url(latitude, longitude):
    return f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"

# Function to capture voice input and convert to text
def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

        try:
            user_input = recognizer.recognize_google(audio)
            st.write(f"User: {user_input}")
            return user_input
        except sr.UnknownValueError:
            st.write("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")
            return None

# Store SOS alert with location URL in Firestore
def store_sos_alert(user_input, ai_response, latitude, longitude, user_data):
    # Generate Google Maps URL if GPS tracking is enabled
    location_url = generate_location_url(latitude, longitude) if user_data['settings']['gps_tracking'] else None
    timestamp = datetime.now()

    # Reference to the device document in Firestore
    device_id = user_data['device_id']
    doc_ref = db.collection("devices").document(device_id)

    sos_data = {
        "DT": timestamp,
        "Trigger_Type": "Voice_command",
        "status": "Active",
        "userId": user_data['email'],  # Assuming user ID is represented by email
        "location_url": location_url,
        "emergency_contacts": user_data['emergency_contacts']
    }

    # Add SOS data under `last_sos` field in the device document
    doc_ref.update({
        "last_sos": sos_data,
        "last_location": {
            "Curr_location": location_url,
            "Timestamp": timestamp
        } if location_url else {}
    })

    # Optionally, you could also keep a history of sent URLs in a subcollection
    doc_ref.collection("sos_history").add(sos_data)

    return location_url

# Function to generate AI response
def generate_response(user_input):
    global chat_history_ids  # Declare chat_history_ids as global to update it
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")

    # Initialize bot_input_ids based on whether chat_history_ids has been initialized
    if chat_history_ids is None:
        bot_input_ids = new_input_ids
    else:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)

    # Generate response and update chat_history_ids
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    ai_response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return ai_response

# Function to convert text to speech and play it
def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    with NamedTemporaryFile(delete=True, suffix='.mp3') as temp_file:
        temp_file_path = temp_file.name
        tts.save(temp_file_path)
        playsound.playsound(temp_file_path)

def main():
    st.title("AI Voice Conversation")
    st.write("Press the button below to start talking to the AI.")

    # Replace with actual user ID as per your setup
    user_id = "IXrrG5Rp41B22fpDOcVC"  # Example document ID in User-Collection
    user_data = get_user_data(user_id)

    if not user_data:
        st.error("User data not found!")
        return

    if st.button("Start Conversation"):
        # Use settings from user data
        latitude = 37.4219983 if user_data['settings']['gps_tracking'] else None
        longitude = -122.084 if user_data['settings']['gps_tracking'] else None

        while True:
            user_input = listen_to_voice()
            if user_input:
                # Generate AI response
                ai_response = generate_response(user_input)
                st.write(f"AI: {ai_response}")

                # Convert AI response to speech and play it
                if user_data['settings']['audio_recording']:
                    text_to_speech(ai_response)

                # Store the SOS alert with location URL in Firestore
                sos_url = store_sos_alert(user_input, ai_response, latitude, longitude, user_data)
                st.write(f"SOS sent! Location: {sos_url if sos_url else 'GPS tracking disabled'}")

if __name__ == "__main__":
    main()
