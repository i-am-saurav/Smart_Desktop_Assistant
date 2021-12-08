import datetime
import pyttsx3
import wikipedia
import speech_recognition as sr
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak('good morning!')
    elif(hour>12 and hour<18):
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')
    speak('I am Babloo sir, how may i help you')

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')
        query=r.recognize_google(audio, language='en-in')
        print(f'user said {query}')
    except Exception as e:
        print('Say that again Please...')
        return 'NONE'
    return query


if __name__ == '__main__':

    wishMe()
    while True:
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open('Youtube.com')

        elif 'google' in query:
            webbrowser.open('Google.com')

        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            musicDir='E:\\Music'
            songs=os.listdir(musicDir)
            print(songs)
            os.startfile(os.path.join(musicDir,songs[0]))

        elif 'open my photo' in query:
            photoDir='E:\\photos\\dslr'
            photo=os.listdir(photoDir)
            print(photo)
            os.startfile(os.path.join(photoDir,random.choice(photo)))

        elif 'wikipedia' in query:
            speak('searching wikipedia')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=2)
            speak(f'According to wikipedia {results}')


        elif 'who are you' in query:
            speak('I am babloo sir, i am a desktop assistant developed by Saurav kumar, i can do some of your task instantly')


        elif 'quit' in query:
            speak('Switching off sir!')
            break
