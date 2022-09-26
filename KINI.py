#our first task is to talk to Kini (My personal assistant) and to talk,she has to understand me.
import speech_recognition as srg 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = srg.Recognizer() #who would be able to understand or recognize my voice by converting spoken words to text.
engine = pyttsx3.init() #this is to intialize the python text to speech.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talking_kini(text):
    engine.say(text)
    engine.runAndWait()

#now, writing the below code in try block because it may happen that sometimes the microphone will not work.
def listening_kini():
    try:
        with srg.Microphone() as source: #using the default microphone as audio source
            print("Speak up....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice) #recognising by google API, you will pass the audio to google and google will give you the text.
            command = command.lower()
            # talking_kini(command)
    except:
        pass
    return command

def taking_commands():
    command = listening_kini()
    if 'play' in command:
        talking_kini('playing')
        command = command.replace('play', '')
        pywhatkit.playonyt(command)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talking_kini('current time is: '+time)
    elif 'tell me' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        talking_kini(info)
    elif 'joke' in command:
        talking_kini(pyjokes.get_joke())
    else:
        talking_kini("Sorry, I cant do this. Please try something else.")
while True:
    taking_commands()