import speech_recognition as sr
import os
import webbrowser
import cohere
import pyttsx3
from config import cohere_api_key  # Secure API key management
import datetime
import random
import numpy as np

chatStr = ""

# Initialize pyttsx3 for text-to-speech
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1)

# Initialize Cohere client
co = cohere.Client(cohere_api_key)


def say(text):
    """Speak function using pyttsx3"""
    engine.say(text)
    engine.runAndWait()


def chat(query):
    """Handle AI chat using Cohere API"""
    global chatStr
    print(chatStr)

    chatStr += f"User: {query}\nJarvis: "

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=query,
            max_tokens=256,
            temperature=0.7
        )

        reply = response.generations[0].text
        say(reply)
        chatStr += f"{reply}\n"
        return reply

    except cohere.CohereError as e:
        say("There was an error connecting to Cohere.")
        return str(e)


def ai(prompt):
    """Save AI-generated response to a file"""

    text = f"Cohere response for Prompt: {prompt} \n *************************\n\n"

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=256,
            temperature=0.7
        )

        text += response.generations[0].text

        if not os.path.exists("Cohere_Responses"):
            os.mkdir("Cohere_Responses")

        filename = f"Cohere_Responses/{''.join(prompt.split('intelligence')[1:]).strip()}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)

    except cohere.CohereError as e:
        say("An error occurred while saving the AI response.")
        print(e)


def takeCommand():
    """Voice recognition function"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            return "Some error occurred. Sorry from Jarvis."


def play_random_song(folder_path):
    """Randomly selects and plays a song from the specified folder"""
    if os.path.exists(folder_path):
        songs = [os.path.join(folder_path, song) for song in os.listdir(folder_path) if song.endswith(('.mp3', '.wav'))]

        if songs:
            random_song = random.choice(songs)
            say(f"Playing {os.path.basename(random_song)} now...")
            os.startfile(random_song)
        else:
            say("No music files found in the specified folder.")
    else:
        say("The provided folder path does not exist.")


if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis AI made by Aditya is now online")

    while True:
        query = takeCommand()

        # Open websites
        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.org",
            "google": "https://www.google.com"
        }

        for site, url in sites.items():
            if f"open {site}" in query:
                say(f"Opening {site}, sir...")
                webbrowser.open(url)

        # Play random music from a given folder
        if "play music" in query:
            music_folder = input("Enter the path to your music folder: ")
            play_random_song(music_folder)

        # Tell the time
        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} hours and {minute} minutes.")

        # Open predefined shortcuts
        elif "open instagram" in query:
            shortcut_path = input("Enter the path for Instagram shortcut: ")
            if os.path.exists(shortcut_path):
                say("Opening Instagram now...")
                os.startfile(shortcut_path)
            else:
                say("Instagram shortcut not found.")

        elif "open zoom" in query:
            shortcut_path = input("Enter the path for Zoom shortcut: ")
            if os.path.exists(shortcut_path):
                say("Opening Zoom now...")
                os.startfile(shortcut_path)
            else:
                say("Zoom shortcut not found.")

        elif "open pass" in query:
            say("Passky app is unavailable on Windows.")

        # AI-powered response generation
        elif "using artificial intelligence" in query:
            ai(prompt=query)

        # Exit command
        elif "jarvis quit" in query or "exit" in query:
            say("Goodbye, see you later!")
            break

        # Reset chat history
        elif "reset chat" in query:
            chatStr = ""

        # General AI chat responses
        else:
            print("Chatting...")
            chat(query)