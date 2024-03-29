
from asyncio import subprocess
from http import client, server
from time import sleep
from traceback import print_tb
from cv2 import haveImageReader
import wolframalpha
from playsound import playsound
import webbrowser
import random
import pyttsx3
import pyaztro
import datetime
import speech_recognition as sr
import wikipedia
import os
import requests
import pywhatkit
import json
import qrcode
import pyautogui as pt
import socket
from dotenv import load_dotenv
from ecapture import ecapture as ec
import time
import nasapy
import urllib.request
from IPython.display import Image,display,Audio
from gtts import gTTS
from PIL import Image
load_dotenv('.env') 


engine = pyttsx3.init('espeak')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices[20].id)  # voice of my doraemom!

WAKE = "nobita"


def speak(audio):  # speak function for doraemon
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 6 and hour < 12:  # morning time
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:  # afternoon time
        speak("Good Afternoon!")
    elif hour >= 18 and hour < 24:  # evening time
        speak("Good Evening!")
    else:
        speak("It's too late. Let me sleep and you too should sleep")

    # created on 1 August 2022
    speak("Hello , I am doraemon. How can I help you?")


def takeCommand(dur):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Doraemon in listening...")
        r.pause_threshold = 1
        audio = r.record(source, dur)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":

    lists = ["khairiyat.mp3", "besabriyaan.mp3", "dil.mp3", "hawayein.mp3", "kun.mp3",
             "namo.mp3", "nights.mp3", "stereo.mp3"]  # list of some random songs i have added
    while True:
      text = takeCommand(3).lower()

      if text.count(WAKE) > 0:
        speak("I am ready")

        wishMe()  # starting with a wishing
        # taking the command for 5 seconds and then converting to lower case
        query = takeCommand(5).lower()
       # searching in wikipedia and then speaking and printing 4 lines from it.
        if 'wikipedia' in query:
            speak('Searching ....')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            print(results)
            speak("From Wikipedia I have collected ,")
            speak(results)
        elif 'open youtube' in query:  # opening youtube
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:  # opening fb
            webbrowser.open("facebook.com")
        elif 'open github' in query:  # opening github
            webbrowser.open("github.com")
        elif 'open google' in query:  # opening google
            webbrowser.open("google.com")
        elif 'open instagram' in query:  # opening insta
            webbrowser.open("instagram.com")
        elif 'open my homepage' in query:  # opening my iitk homepage
            webbrowser.open("home.iitk.ac.in/~guptah20/")
        elif 'i love you doraemon' in query:  # pouring love
            speak("I Love you too !")
        elif 'who made you' in query:  # credits
            speak("Harshit Gupta created me with love in August 2022")
        elif 'song' in query:  # playing random song
            integer = random.randrange(0, 7)
            playsound(lists[integer])
        elif 'time' in query:  # asking for time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is, {strTime}")
        elif 'date' in query:  # asking date
            print(datetime.date.today())
        elif 'log out' in query or 'sign out' in query:  # logging out from my linux system
            os.system('pkill -KILL -u harshit')
        elif "take a photo" in query:
            ec.capture(0, "Doraemon", "img.jpg")  # looking good? take a photo and find out!
        elif 'search' in query:  # searching on google or duckduck go
            speak("Where do you want to search? In google or in duck duck go?")
            s_engine = takeCommand(5).lower()
            if 'google' in s_engine:
                speak("What do you want to search?")
                ques = takeCommand(10)
                pywhatkit.search(query)
            else:
                # making url for search on duck duck go
                speak("What do you want to search?")
                que = takeCommand(10)
                que = que.replace(" ", "+")
                pp = "q="
                ee = "&t=h_&ia=web"
                tabUrl = "https://www.duckduckgo.com/?"
                print(tabUrl+pp+que+ee)
                webbrowser.open_new_tab(tabUrl+pp+que+ee)
        elif 'answer' in query:  # geo questions from api
            speak(
                "I can answer to computational and geographical questions. please ask me ")
            question = takeCommand(10)
            app_id = os.getenv('answer')
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
        elif "don't listen" in query or "stop listening" in query:   # want to do some personal work before using doraemon?
            speak("for how much time you want to stop me from listening you")
            a = int(takeCommand(3))
            time.sleep(a)

        elif 'weather of' in query:  # asking for weather of a city
            api_key = os.getenv('api_key')
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
                resp_string = " The temperature in Kelvin is, " + \
                    str(temp) + " The humidity is, " + str(hum) + \
                    " and The weather description is, " + str(desc)
                print(resp_string)
                speak(resp_string)
            else:
                speak("City Not Found")
        elif 'send message' in query:  # sending whatsapp msg by number
            speak("How do you want to send message, by audio or by typing?")
            query = takeCommand(4).lower()
            if 'typing' in query:
                speak("Please Write the number")
                number = input()
                speak("Please write what should I send")
                message = input()
                time = datetime.datetime.now()
                pywhatkit.sendwhatmsg_instantly(
                    "+91"+number, message, 30, True)
            elif 'audio' in query:
                speak("Please tell me the number.")
                number = takeCommand(12)
                speak("Please send me the message you want me to convey for you")
                message = takeCommand(20)

                time = datetime.datetime.now()
                pywhatkit.sendwhatmsg_instantly(
                    "+91"+number, message, 30, True)
        elif 'book pdf' in query:  # searching for a book pdf on z-lib
            speak("Which book you want to have?")
            book = takeCommand(8)
            book.replace(" ", "%20")
            webbrowser.open("https://1lib.in/s/book")
        elif 'encode' in query:  # encodig a webpage or a text in the form of qr code.

            speak("Please write what you want to encode.")
            xx = input()

            img = qrcode.make(xx)
            img.save("qr.png", "PNG")
        elif 'ip' in query:  # ip address
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            print(s.getsockname()[0])
            s.close()
        elif 'horoscope' in query:  # Beleive in horoscope?
            speak("For which sign you want to get horoscope?")
            ans = takeCommand(5)
            sign_person = pyaztro.Aztro(sign=ans)

            print( ans , ': \n',
                  'Sign:',             sign_person.sign,          '\n',
                  'Current date:',     sign_person.current_date,  '\n',
                  'Date range:',       sign_person.date_range,    '\n',
                  'Sign description:', sign_person.description,   '\n',
                  'Mood:',             sign_person.mood,          '\n',
                  'Compatibility:',    sign_person.compatibility, '\n',
                  'Lucky number:',     sign_person.lucky_number,  '\n',
                  'Lucky time:',       sign_person.lucky_time,    '\n',
                  'Lucky color:',      sign_person.color,       2*'\n',)
        elif 'goodbye' in query:
            speak("Goodbye dear. Hope we'll meet soon.")
            break
        elif 'picture of day' in query: # an astronomy fan?
            nasa = os.getenv('nasa')
            
            nasax = nasapy.Nasa(key =nasa)
            d = datetime.date.today().strftime('%Y-%m-%d')
            apod = nasax.picture_of_the_day(date=d, hd=True)
            if(apod["media_type"] == "image"):
               if("hdurl" in apod.keys()):
                   title = d + "_" + apod["title"].replace(" ","_").replace(":","_") + ".jpg"
                   image_dir = "./Astro_Images"
                   dir_res = os.path.exists(image_dir)
                   if (dir_res==False):
                     os.makedirs(image_dir)


                   urllib.request.urlretrieve(url = apod["hdurl"] , filename = os.path.join(image_dir,title))
                #    img = Image.open( os.path.join(image_dir,title))
                #    img.show()
                   webbrowser.open(os.path.join(image_dir,title))
                   print("Date image released: ",apod["date"])
                   print("\n")
                   if("copyright" in apod.keys()):
                    print("This image is owned by: ",apod["copyright"])
                    print("\n")
                   print("Title of the image: ",apod["title"])
                   print("\n")
                   print("Description for the image: ",apod["explanation"])
                   print("\n")
                  
                   
            else:
                print("Sorry, Image not available!")
        elif 'mars rover' in query: # wanna see puctures of mars rover curiosity?
             har = os.getenv('api_nasa')
            
             f = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&"
             f = f + "api_key=" + har
             print(f)
             data = requests.get(f)
             a = json.loads(data.text)
             print(a)
             for i in a["photos"]:
               print(i, "\n\n\n")
    
             b = a["photos"][0]["img_src"]
    
             webbrowser.open(b)
        elif 'fun' in query: # Getting bored? Doraemon is here!
            f = "http://www.boredapi.com/api/activity/"
            data = requests.get(f)
            json_data = data.json()
            act_data = json_data["activity"]
            act_type = json_data["type"]
            speak(act_data,)
            print(act_data)

            speak("It is of type" + act_type)
