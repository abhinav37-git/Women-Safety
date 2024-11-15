import streamlit as st
import speech_recognition as sr
from transformers import AutoModelForCausalLM, AutoTokenizer
from gtts import gTTS
import os
import torch
import playsound
from tempfile import NamedTemporaryFile

# Load a pre-trained DialoGPT model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Keep conversation history to maintain context
chat_history_ids = None

# Function to capture voice input and convert to text
def listen_to_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

        try:
            # Convert voice to text
            user_input = recognizer.recognize_google(audio)
            st.write(f"User: {user_input}")
            return user_input
        except sr.UnknownValueError:
            st.write("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")
            return None

# Generate AI response using DialoGPT
def generate_response(user_input):
    global chat_history_ids

    # Tokenize input with attention mask
    new_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    attention_mask = torch.ones(new_input_ids.shape, dtype=torch.long)

    # Append new input to chat history
    if chat_history_ids is not None:
        bot_input_ids = torch.cat([chat_history_ids, new_input_ids], dim=-1)
        attention_mask = torch.cat([torch.ones(chat_history_ids.shape, dtype=torch.long), attention_mask], dim=-1)
    else:
        bot_input_ids = new_input_ids

    # Generate a response with attention mask
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, attention_mask=attention_mask, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# Convert AI response to speech using gTTS and play the audio
def text_to_speech(text):
    tts = gTTS(text)
    
    # Save to a temporary file
    with NamedTemporaryFile(delete=True) as tmp_file:
        tts.save(tmp_file.name)
        playsound.playsound(tmp_file.name)

# Main function for the Streamlit app
def main():
    st.title("AI Voice Conversation")
    st.write("Press the button below to start talking to the AI.")
    
    if st.button("Start Conversation"):
        user_input = listen_to_voice()
        if user_input:
            # Generate AI response
            ai_response = generate_response(user_input)
            st.write(f"AI: {ai_response}")
            
            # Convert AI response to speech and play it
            text_to_speech(ai_response)

if __name__ == "__main__":
    main()
