## Introduction

This project is a voice-prompt based safety device for women, leveraging the power of Generative AI. The device is designed to provide quick and efficient assistance in emergency situations through voice commands.

## Features

- **Voice Activation**: The device can be activated using specific voice commands such as "HELP", "SHOUTING NOISE", "DISTRESS VOICE".
- **Real-time Assistance**: Provides immediate help by sending sos signals to emergency contact along with google maps tracking link.

## Technologies Used

- **Python**: The core programming language used for development.
- **Streamlit**: Used for building the web application interface.
- **Generative AI Models**: Implemented for voice recognition and response generation, microsofts dialogueGPT model.
- **Firebase**: For logging the device, event activity, and user data.

## Project Setup

### Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

### Setting Up the Environment

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

### Running the Project

1. **Start the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2. **Open your web browser and go to:**

    ```
    http://localhost:8501
    ```

### Project Structure

- `main3.py`: Main application file for Streamlit.
- `requirements.txt`: List of dependencies required for the project.

## Contributing

We welcome contributions to enhance the functionality and features of this project. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

