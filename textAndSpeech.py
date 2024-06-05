import streamlit as st
import speech_recognition as sr
import pyttsx3

if 'recording' not in st.session_state:
    st.session_state.recording = False

# Initialize the recognizer
r = sr.Recognizer()

class TextAndSpeech:
    def __init__(self):
        """
        Initialize the TextAndSpeech class.
        """
        self.engine = pyttsx3.init()

    def speak_text(self, command):
        """
        Convert text to speech.

        Parameters:
        - command (str): The text to be spoken.
        """
        engine = pyttsx3.init()
        self.engine.say(command)
        self.engine.runAndWait()

    def record(self):
        """
        Record audio using the microphone.

        Returns:
        - audio (sr.AudioData): The recorded audio data.
        """
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            st.toast("🎤 Recording...")
            audio = r.listen(source)
            st.session_state.recording = False
            return audio

    def analyze(self, audio):
        """
        Analyze the recorded audio and convert it to text.

        Parameters:
        - audio (sr.AudioData): The recorded audio data.

        Returns:
        - text (str): The recognized text from the audio or an error message.
        """
        try:
            text = r.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "er"
        except sr.RequestError as e:
            st.write(f"Could not request results; {e}")
            return "er"
