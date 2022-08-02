
from asyncio import subprocess
from http import client, server
from traceback import print_tb
import wolframalpha
from playsound import playsound
import webbrowser
import random
import pyttsx3
import datetime 
import speech_recognition as sr
import wikipedia
import os
import requests
import pywhatkit
import json
import qrcode

import pyautogui as pt
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

def takeCommand(dur):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Doraemon in listening...")
        r.pause_threshold = 1
        audio = r.record(source,dur)
        

    try:
        print("Understanding...")
        query = r.recognize_google(audio,language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"   
    return query   


def takeMessage():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Doraemon in listening...")
        r.pause_threshold = 10
        audio = r.listen(source,None,120)
        

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
    lists = ["khairiyat.mp3", "besabriyaan.mp3" ,"dil.mp3", "hawayein.mp3"  ,"kun.mp3", "namo.mp3", "nights.mp3","stereo.mp3"]
    while True:
       
        query = takeCommand(4).lower()

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
            speak("Harshit Gupta created me with love in August 2022")  
        elif 'play songs' in query:
            integer = random.randrange(0,7)
            playsound(lists[integer])    
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")             
            speak(f"The time is, {strTime}") 
        elif 'log out' in query or 'sign out' in query:
            os.system('pkill -KILL -u harshit')    
        elif 'search' in query:
            statement = query.replace(" search","")
            statement = statement.replace(" ","+")
            pp= "q="
            ee = "&t=h_&ia=web"
            tabUrl = "https://www.duckduckgo.com/?"
            print(tabUrl+pp+statement+ee)
            webbrowser.open_new_tab(tabUrl+pp+statement+ee)   
        elif 'what else can you do' in query:
            speak("I can answer to computational and geographical questions. please ask me ")
            question = takeCommand(10)
            app_id="JQ6L9G-4G894PW2YG"
            client = wolframalpha.Client('JQ6L9G-4G894PW2YG')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)     
        elif 'weather of' in query:
            api_key="331857c0b5e9a4840523810a1392cfa3"
            
            weather_url = "http://api.openweathermap.org/data/2.5/weather?"
            query = query.split(" ")
            location = str(query[2])
            url = weather_url + "appid=" + api_key + "&q=" + location 
            js = requests.get(url).json() 
            if js["cod"] != "404": 
                 weather = js["main"] 
                 temp = weather["temp"] 
                 hum = weather["humidity"] 
                 desc = js["weather"][0]["description"]
                 resp_string = " The temperature in Kelvin is " + str(temp) + " The humidity is " + str(hum) + " and The weather description is "+ str(desc)
                 print(resp_string)
                 speak(resp_string)
            else: 
                 speak("City Not Found")     
        elif 'send message' in query:
            speak("How do you want to send message, by audio or by typing?")
            query = takeCommand(4).lower()
            if 'typing' in query:
               speak("Please Write the number")
               number = input()
               speak("Please write what should I send")   
               message = input()
               time = datetime.datetime.now()
               pywhatkit.sendwhatmsg_instantly("+91"+number, message,15,True)
            elif 'audio' in query :
                speak("Please tell me the number.")
                number = takeCommand(12)
                speak("Please send me the message you want me to convey for you")
                message = takeMessage()
                time = datetime.datetime.now()
                pywhatkit.sendwhatmsg_instantly("+91"+number, message,15,True)
        elif 'book pdf' in query:
            speak("Which book you want to have?")
            book = takeCommand(8)
            book.replace(" ","%20")
            webbrowser.open("https://1lib.in/s/book")   
        elif 'encode' in query:
            speak("Please write what you want to encode.")
            xx= input()
            
            img = qrcode.make(xx)
            img.save("qr.png", "PNG")
            
           



            
