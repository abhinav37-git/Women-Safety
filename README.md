## Overview
This project aims to provide a comprehensive solution for emergency situations using two different approaches: an AI model-based SOS command and a push-button-based GPS trigger. Both methods are designed to ensure quick and efficient communication of the user's location to emergency services. Following a hybrid development approach, both the methods are implemented in a physical device for better accuracy of the trigger end.

## Table of Contents
1. [AI Model-Based SOS Command](#ai-model-based-sos-command)
2. [Push Button-Based GPS Trigger](#push-button-based-gps-trigger)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Hardware Requirements](#hardware-requirements)
6. [Contributing](#contributing)

### Key Features
- **Voice Recognition**: Utilizes a trained AI model to recognize specific SOS commands.
- **Immediate Response**: Automatically sends the user's GPS location to emergency services upon recognizing the command.
- **Hands-Free Operation**: Ideal for scenarios where the user is unable to use their hands.

### How It Works
1. **Audio Input**: The system continuously listens for audio input.
2. **Command Detection**: The AI model processes the audio and detects the SOS command.
3. **Alert Trigger**: Upon detection, the system sends the user's GPS location to predefined emergency contacts.

## AI Model-Based SOS Command
## Introduction

This project is a voice-prompt based safety device for women, leveraging the power of Generative AI. The device is designed to provide quick and efficient assistance in emergency situations through voice commands.

### Features

- **Voice Activation**: The device can be activated using specific voice commands such as "HELP", "SHOUTING NOISE", "DISTRESS VOICE".
- **Real-time Assistance**: Provides immediate help by sending SOS signals to emergency contacts along with a Google Maps tracking link.

### Technologies Used

- **Python**: The core programming language used for development.
- **Streamlit**: Used for building the web application interface.
- **Generative AI Models**: Implemented for voice recognition and response generation, using Microsoft's DialoGPT model.
- **Firebase**: For logging the device, event activity, and user data.

## Push Button-Based GPS Trigger

### Explanation
The push-button-based GPS trigger is a hardware solution that allows users to send their GPS location to emergency services by pressing a physical button. This method is straightforward and reliable, making it an excellent option for users who may not be able to use voice commands.

### Key Features
- **Physical Activation**: A simple push button that triggers the GPS signal.
- **Immediate Response**: Sends the user's GPS location to emergency contacts instantly.
- **Reliable**: Works even in noisy environments where voice commands may not be effective.

### How It Works
1. **Hardware Setup**: The push button is connected to a microcontroller (e.g., Arduino) that interfaces with a GPS module.
2. **Button Press**: When the button is pressed, the microcontroller reads the GPS coordinates.
3. **Alert Trigger**: The microcontroller sends the GPS coordinates to predefined emergency contacts via a communication module (e.g., GSM, Wi-Fi).

## Installation
### 1. AI Model-Based SOS Command

#### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

#### Setting Up the Environment

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/GenAI-hack-CU.git
    cd GenAI-hack-CU
    ```

2. **Create a new Python virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

4. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

#### Running the Project

1. **Start the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://localhost:8501
    ```

#### Project Structure

- `main3.py`: Main application file for Streamlit.
- `requirements.txt`: List of dependencies required for the project.

### 2. Push Button-Based GPS Trigger

#### Code Example
The Arduino code (`gps.ino`) is used to implement the push-button-based GPS trigger.

## Hardware Requirements
- **Microcontroller**: Arduino or similar.
- **GPS Module**: For obtaining the user's location.
- **Push Button**: For triggering the alert.
- **Communication Module**: GSM, Wi-Fi, or other means to send the GPS data.

## Contributing
We welcome contributions to enhance the functionality and features of this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.
