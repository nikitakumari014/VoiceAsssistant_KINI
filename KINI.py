
import speech_recognition as srg
import pyttsx3
import webbrowser
import time
import subprocess
from ecapture import ecapture as ec
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = srg.Recognizer()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish_user():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, GoodMorning")
        print("Hello, GoodMorning")
    elif hour>=12 and hour<18:
        speak("Hello, GoodAfternoon")
        print("Hello, GoodAfternoon.")
    else:
        speak("Hello, GoodEvening")
        print("Hello, GoodEvening")

def take_command():
   with srg.Microphone() as source:
       print("Listening...")
       audio = listener.listen(source)
       try:
           command=listener.recognize_google(audio,language='en-in')
           print(f"User: {command}\n")
       except:
           speak("Please say that again")
           return "None"
       return command


print("Loading your AI personal Assistant")
speak("Loading your AI personal Assistant")

wish_user()

if __name__ == '__main__':

    while True:
        speak("Tell me how can i help you?")
        command=take_command().lower()
        if command==0:
            continue
        elif "goodbye" in command or "ok bye" in command or "stop" in command:
            speak("KINI is shutting down ByeBye")
            print("KINI is shutting down. ByeBye")
            break;
        elif 'tell me' in command:
            speak("Searching on wikipedia...")
            command = command.replace('tell me about', '')
            info = wikipedia.summary(command, sentences=3)
            speak("According to Wikipedia")
            print(info)
            speak(info)
            continue
        elif 'play' in command:
            speak('playing')
            command = command.replace('play', '')
            pywhatkit.playonyt(command)
        elif 'whatsApp' in command:
            speak("Opening WhatsApp")
            webbrowser.open("whatsApp.com")
            time.sleep(5)
        elif 'youtube' in command:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("Youtube is open now")
            time.sleep(5)
        elif 'google' in command:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is open now")
            time.sleep(5)
        elif 'gmail' in command:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Gmail is open now")
            time.sleep(5)
        elif 'time' in command:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is: {strtime}")
        elif 'news' in command:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines of today")
            time.sleep(8)
        elif 'camera' in command or 'photo' in command:
            ec.capture(0, "KINI camera", "image.jpg")
        elif 'search' in command:
            command = command.replace('search','')
            webbrowser.open_new_tab(command)
            time.sleep(6)
        elif 'who are you' in command or 'what can you do' in command:
            speak("I am KINI,your personal voice assistant. "
                  "I am programmed to do minor things like playing a song, "
                  "opening a googlechrome, gmail,news.")
            print("I am KINI,your personal voice assistant. "
                  "I am programmed to do minor things like playing a song, "
                  "opening a googlechrome, gmail,news.")
        elif 'who made you' in command or 'who created you' in command:
            speak("I was programmed by my Master Niki. "
                  "And that's why i have been named as KINI")
            print("I was programmed by my Master Niki. "
                  "And that's why i have been named as KINI")
        elif 'shutdown' in command:
            speak("okay, your pc will shutdown in just 10 seconds.")
            subprocess.call(["shutdown", "/1"])
        elif 'write a note' in command:
            speak("What i have to write?")
            note = take_command()
            file = open('jarvis.txt','w')
            speak("Should i include date also?")
            reply = take_command()
            if 'yes' in reply:
                strtime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strtime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif 'show note' in command:
            speak("Have you written anything recently?")
            reply = take_command()
            if 'yes' in reply:
                file = open("jarvis.txt","r")
                print(file.read())
                speak(file.read(6))
        elif 'joke' in command:
            speak(pyjokes.get_joke())
        elif 'stackoverflow' in command:
            webbrowser.open('stackoverflow.com')
        else:
            speak("Sorry, I can't do that Tell me something else to do")

time.sleep(3)
