import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def talk(text):
 engine.say(text)
 engine.runAndWait()

def take_command():
 try:
    with sr.Microphone() as source:
        voice=listener.listen(source)
        command=listener.recognize_google(voice)
        command=command.lower()
        if 'alexa' in command:
            command=command.replace('alexa','')
            print(command)
 except:
    pass
 return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song =command.replace('play', '')
        talk('playing' +song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time= datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Hi Sir current time is'+time)
    elif 'tell me' or 'who' or 'who is' or 'what about' or 'define' or 'wikipedia' or 'what is' or 'what are' in command:
        result=wikipedia.summary(command,2)
        print(result)
        talk(result)
    elif 'joke' in command:
        result=pyjokes.get_joke()
        print(result)
        talk(result)
    elif 'open' in command:
        location= 'D:\\'
        loc=os.listdir(location)
        print(loc)
        os.startfile(os.path.join(location))
    else:
        talk('sorry sir i did not get can you repeat')

run_alexa()