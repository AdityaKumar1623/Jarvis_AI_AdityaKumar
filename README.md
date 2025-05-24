# Jarvis AI 🤖🚀
A Python-based AI assistant using voice recognition and Cohere NLP for intelligent interactions


**Jarvis AI** is a sophisticated, voice-activated personal assistant built in Python and powered by Cohere’s advanced NLP. Transform your spoken words into digital magic as Jarvis automates your daily tasks and streamlines your interactions with technology! ✨💡

---

## Table of Contents
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Setup & Configuration](#setup--configuration)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features 🚀

- **Voice Command Mastery 🗣️💬:**  
  Simply speak a command, and Jarvis springs into action—launching websites, playing music, navigating your system, and more!
  
- **Unified Automation 🔄⚡:**  
  No matter what you need, Jarvis integrates and executes your commands, turning ideas into reality in an instant.
  
- **Smart Integration 🤖🔗:**  
  By harnessing dynamic libraries and APIs, Jarvis learns and adapts to your voice commands to create a truly personalized digital assistant.
  
- **Robust Library Backbone 📚:**  
  Built with:
  - `speech_recognition` for capturing your voice commands 🎙️
  - `pyttsx3` to convert text into natural speech 🗣️
  - `cohere` for generating intelligent responses using advanced NLP 🤓
  - Plus, standard libraries like `os`, `webbrowser`, `datetime`, `random`, and `numpy` to handle various system functions.

---

## Demo 🎥

*(Insert a demo video link or screenshots here if available)*

---

## Installation 💻

### Prerequisites
- **Python 3.6+** 🐍
- A functioning **microphone** and **speakers** 🎤🔊
- A valid **Cohere API key** 🔑

### Dependencies
Install the required Python packages by running:

```bash
pip install speechrecognition pyttsx3 cohere numpy
```

> **Note:** For enhanced voice recognition support on Windows, you might need to install `PyAudio`:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

---

## Setup & Configuration ⚙️

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/yourusername/JarvisAI.git
    cd JarvisAI
    ```

2. **Configure Your API Key:**

    Create a file called `config.py` in the root directory and add your Cohere API key:

    ```python
    cohere_api_key = "YOUR_COHERE_API_KEY"
    ```

3. **Update Shortcut Paths:**

    Modify the file paths within `jarvis.py` (e.g., music folder, Instagram, Zoom shortcuts) to match your system configuration.

---

## Usage 🚀

Run the application by executing:

```bash
python jarvis.py
```

When you launch Jarvis AI, it will greet you with a voice prompt and start listening for your commands. Here are some examples:

- **"open YouTube"** – Launches your favorite website.
- **"play music"** – Randomly selects and plays a song from your designated folder.
- **"the time"** – Announces the current time.
- **"open instagram"** or **"open zoom"** – Opens predefined desktop shortcuts.
- **"using artificial intelligence"** – Generates an AI response and saves it to a file.
- **"jarvis quit"** or **"exit"** – Stops the application.
- **"reset chat"** – Clears the conversation history.

Jarvis runs continuously until you decide to exit. Enjoy the seamless interaction! 💡

---

## Code Overview 📝

- **`jarvis.py`**
  - The main entry point for the project, managing voice input, text-to-speech, AI response generation, and system commands.
  
- **Key Functions:**
  - **`say(text)`** – Uses `pyttsx3` to convert text to speech.
  - **`takeCommand()`** – Captures voice input via `speech_recognition` and converts it to text.
  - **`chat(query)`** – Sends your queries to Cohere’s API to generate conversational responses while maintaining a chat history.
  - **`ai(prompt)`** – Generates AI-powered responses and saves them to the `Cohere_Responses` folder.
  - **`play_random_song(folder_path)`** – Randomly selects and plays a music file from a specified folder.

---

## Contributing 🛠️

Contributions are very welcome! If you’d like to extend Jarvis AI’s functionalities, fix issues, or improve documentation, please open an issue or submit a pull request. Let's build something amazing together! 🤝

---

## License 📄

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements 🙏

- **[Cohere](https://cohere.com)** – Empowering Jarvis with advanced NLP capabilities.
- **[speech_recognition](https://github.com/Uberi/speech_recognition)** – For enabling robust voice input.
- **[pyttsx3](https://github.com/nateshmbhat/pyttsx3)** – For natural text-to-speech functionality.
- Thanks to the open-source community for their invaluable contributions and support!

---

Feel free to further customize this README to match your unique style and project specifics. Happy coding! 🎉
