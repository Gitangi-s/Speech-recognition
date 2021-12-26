# Speech-recognition

from gtts import gTTs
import os
voice = ""
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = r.listen(source)
            text = r.recognize_google(audio)
            print(text)
            if text =="stop":
                break
            text = r.recognize_google(audio)
            voice = voice + str(text)
        expect:
        print("Say something....")
hr = gTTs(text=voice, Lang='en', slow=False)
hr.save("1.wav")
