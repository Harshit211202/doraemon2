import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')

engine.setProperty('voices',voices[20].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:      #morning time
        speak("Good Morning!")
    elif hour>=12 and hour<18:   #afternoon time
        speak("Good Afternoon!")  
    elif hour>=18 and hour<22:   #evening time
        speak("Good Evening!")
    else:                        #night
        speak("Good Night!")

    speak("Hello , I am doraemon. How can I help you?") # created on 1 August 2022

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Doraemon in listening...")
        r.pause_threshold = 1
        audio = r.record(source,5)
        

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"   
    return query   

if __name__ ==  "__main__":  
    wishMe() #starting

    while True:
        
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching ....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=4)
            print(results)
            speak("From Wikipedia I have collected ,")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open github' in query:
            webbrowser.open("github.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com") 
        elif 'open my homepage' in query:
            webbrowser.open("home.iitk.ac.in/~guptah20/")   
        elif 'i love you doraemon' in query:
            speak("I Love you too darling!")     
        elif 'who has made you?' in query:
            speak("Harshit Gupta created me with love")          