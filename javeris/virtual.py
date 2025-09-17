import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# Set the voice (you can try changing the index to 0 or 1 to get a different voice)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    """Speaks the given audio text."""
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    """Wishes the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your personal assistant. How can I help you?")

def take_command():
    """Listens for the user's voice command and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300  # Adjust as needed for your environment's ambient noise
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio, language='en-in')
        print(f"User said: {command}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return command

if __name__ == "__main__":
    wish_me()
    while True:
        command = take_command().lower()

        # Logic for executing tasks based on command
        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            try:
                results = wikipedia.summary(command, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.PageError:
                speak("Sorry, I could not find any results on Wikipedia for that query.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")
        
        elif 'open youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
        
        elif 'open google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
            
        elif 'open stack overflow' in command:
            webbrowser.open("https://stackoverflow.com")
            speak("Opening Stack Overflow.")

        elif 'play music' in command:
            music_dir = 'C:\\Users\\YourName\\Music' # Replace with the actual path to your music folder
            songs = os.listdir(music_dir)
            if songs:
                # Play a random song from the directory
                os.startfile(os.path.join(music_dir, random.choice(songs)))
                speak("Playing a random song from your music folder.")
            else:
                speak("I could not find any music files in the specified directory.")

        elif 'the time' in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The time is {current_time}")

        elif 'the date' in command:
            today = datetime.date.today().strftime("%B %d, %Y")
            speak(f"Today's date is {today}")

        elif 'how are you' in command:
            responses = ["I'm doing well, thank you for asking!", "I'm functioning optimally.", "All systems are running smoothly."]
            speak(random.choice(responses))

        elif 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break
