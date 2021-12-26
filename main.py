import speech_recognition as sr
import pyttsx3

listener = sr.recognizer()
engine = pyttsx3.init()
voices = engine.getProprty('voices')
engine.getProperty('voices',voices[1].id)

def talk(text):
    engine.say(text)
    engine.runandwait()

try:
    with sr.microphone() as source:
        print('Listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if ('Alexa') in command:
        talk(command)
except:
    pass

