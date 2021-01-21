from plyer import notification
import speech_recognition as sr
import pyttsx3
import os
from calc import *
import subprocess
from open_apps import openApp
import webbrowser as wb
import wikipedia
import json
import requests
import geocoder
from geopy.geocoders import Nominatim
from welcome import *
import screen_brightness_control as sbc
from time import *
from youtube_downloader import *
from math import *
from azan import *
from voice_activation import *
from words import *
from app_closer import closeApp
from pyttsx3.drivers import sapi5
r = sr.Recognizer()

engine = pyttsx3.init()


numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
v = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
     "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"]
data = json.load(open('user.json',))
username = data["username"]
city = data["city"]
voice = data["voice"]


def main():
    global username
    global city
    global voice
    if username == "":
        Speak("Hello. I'm your virtual assistant. What's your name?")
        username = input(
            "Hello I'm your virtual assistant What's your name?\n")
        data = json.load(open('user.json', ))
        data["username"] = username
        with open("user.json", "w") as f:
            f.write(json.dumps(data))
    if city == "":
        while True:
            Speak("Please enter your city")
            city = input("Please Enter Your City :\n")
            geolocator = Nominatim(user_agent='myapplication')
            location = geolocator.geocode(city)
            if location != None:
                break
        data = json.load(open('user.json', ))
        data["city"] = city
        with open("user.json", "w") as f:
            f.write(json.dumps(data))

    if voice == "":
        for a in range(len(v)):
            engine.setProperty('voice', (v[a]))
            Speak(
                f"For this voice press {a}")
        c = input("Please Choose (0, 1) :")

        while (c != "0" and c != "1"):
            c = input("Please Choose (0, 1) :")

        c = int(c)

        data = json.load(open('user.json', ))
        data["voice"] = c
        with open("user.json", "w") as f:
            f.write(json.dumps(data))
        voice = data["voice"]

    voices = engine.getProperty('voices')

    engine.setProperty(
        'voice', v[int(voice)])

    Speak(f"Good {welcome_mesage()} {username}")
    Speak(
        f"it is {int(strftime('%I'))} {int(strftime('%M'))} {strftime('%p')}")

    while True:

        try:
            calc = False
            with sr.Microphone() as source2:
                print("Adjusting Audio")
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("Listening")
                audio2 = r.listen(source2)
                print("Processing The Data ")
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                print("You said :"+MyText)

                # Replace numbers for Calculator
                MyText = replace_theTexting_by_num(MyText)
                for i in MyText:
                    if i in numbers:
                        calc = True

                if calc == True:
                    MyText = replace_expresions(MyText)

                # Say Hello
                if "hello" in MyText:
                    Speak("Hello to you too!")

                if "+" in MyText or "-" in MyText or "*" in MyText or "/" in MyText or "sqrt" in MyText:
                    try:
                        result = eval(MyText)
                        Speak(f"The answer is {result}")
                        print(f"The answer is {result}")

                    except:
                        Speak("What was That ?")

                elif "weather" in MyText:
                    Speak(
                        f"The weather in {city} is {weather_message()[0]}  degrees ,  and {weather_message()[1]}")

                elif "date" in MyText:
                    Speak("Today is " + str(strftime('%A')) + str(int(strftime('%d'))) +
                          str(strftime('%B')) + str(strftime('%Y')))

                elif "azan" in MyText or "pray" in MyText:
                    Speak(get_prayer())

                elif "time" in MyText:
                    Speak(
                        f"it is {int(strftime('%I'))} {int(strftime('%M'))} {strftime('%p')}")

                elif "change" in MyText and "name" in MyText:
                    Speak("What's your name?")
                    username = input(
                        "What's your name?\n")
                    data = json.load(open('user.json', ))
                    data["username"] = username
                    with open("user.json", "w") as f:
                        f.write(json.dumps(data))

                elif "change" in MyText and "city" in MyText:
                    while True:
                        Speak("Please enter your new city")
                        city = input("Please Enter Your New City :\n")
                        geolocator = Nominatim(user_agent='myapplication')
                        location = geolocator.geocode(city)
                        if location != None:
                            break
                    data = json.load(open('user.json', ))
                    data["city"] = city
                    with open("user.json", "w") as f:
                        f.write(json.dumps(data))

                # Voice Changing
                elif "change" in MyText and "voice" in MyText:
                    for a in range(len(v)):
                        engine.setProperty('voice', (v[a]))
                        Speak(
                            f"For this voice press {a}")
                    while True:
                        c = input("Please Choose (0, 1) :")
                        if c in ("0", "1"):
                            c = int(c)
                            break
                    data = json.load(open('user.json', ))
                    data["voice"] = c
                    with open("user.json", "w") as f:
                        f.write(json.dumps(data))

                    voices = engine.getProperty('voices')

                    engine.setProperty(
                        'voice', v[int(c)])

                # Notes
                elif "note" in MyText:
                    if "take" in MyText:
                        with open("notes.txt", "a") as f:
                            Speak("Please Type Your Notes")
                            notes = input("Please Type Your Notes :\n")
                            f.write(notes + "\n")
                    elif "delete" in MyText or "remove" in MyText:
                        Speak("Your Notes Will Be Deleted. Are You Sure")
                        notes = input("Are you sure (Y/N):\n")
                        if notes.lower() == "y":
                            with open("notes.txt", "w") as f:
                                f.write("")
                    else:
                        with open("notes.txt", "r") as f:
                            Speak(f.read())

                # Open Programmes
                elif "open" in MyText:
                    MyText = MyText.replace("open ", "")
                    x = openApp(MyText)
                    if not x:
                        Speak("Here's some results from the internet")
                    else:
                        Speak(f"opening {str(MyText)}")

                # Google Search
                elif "google" in MyText:
                    search = MyText.replace(
                        "google ", "")
                    wb.open_new_tab(
                        f'https://www.google.com/search?q={search}')

                elif "what is" in MyText:
                    search = MyText.replace("what is ", "")
                    try:
                        print(wikipedia.summary(search))
                        Speak("According to wikipedia " +
                              wikipedia.summary(search))
                    except:
                        search = MyText.replace(
                            "what is ", "")
                        wb.open_new_tab(
                            f'https://www.google.com/search?q={search}')

                elif "download" in MyText and "youtube" in MyText:
                    Speak("Please type the video you want to download")
                    url = input("Please type the video you want to download :")
                    youtube_download(url)
                # Brightness Control
                elif "brightness" in MyText:
                    old = sbc.get_brightness()
                    if "increase" in MyText or "raise" in MyText:
                        sbc.set_brightness(old + 25)
                        Speak(f"increasing brightness")
                    elif "max" in MyText:
                        sbc.set_brightness(100)
                        Speak(f"maximum brightness")
                    elif "decrease" in MyText or "lower" in MyText:
                        Speak(f"decreasing brightness")
                        sbc.set_brightness(old - 25)
                    elif "min" in MyText:
                        Speak(f"Mnimun brightness")
                        sbc.set_brightness(0)
                    else:
                        Speak(f"Current brightness is {old}")

                elif "close" in MyText:
                    MyText = MyText.replace("close ", "")
                    Speak(f"Closing {MyText}")
                    x = closeApp(MyText)
                    if not x:
                        Speak(f"Nothing found")
                    else:
                        Speak(f"{x} Closed")

                # Shutdown
                elif "shutdown" in MyText or "shut down" in MyText:
                    if "after" in MyText:
                        time = ((get_hours(MyText) * 3600 +
                                 get_minutes(MyText) * 60))
                        os.system(f"Shutdown -s -t {time}")
                    else:
                        for i in range(11, 0, -1):
                            print(f"Shutting down in {i}")
                            sleep(1)
                        os.system("shutdown -s")

                # restart
                elif "restart" in MyText:
                    if "after" in MyText:
                        time = ((get_hours(MyText) * 3600 +
                                 get_minutes(MyText) * 60))
                        os.system(f"Shutdown -r -t {time}")
                    else:
                        for i in range(11, 0, -1):
                            print(f"Restarting in {i}")
                            sleep(1)
                        os.system("shutdown -r")
                elif "bye" in MyText or "quit" in MyText or "leave" in MyText:
                    Speak("it was an honor serving here ")
                    quit()

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")

        word = get_word("stand_by")
        notification.notify(
            title='Standing By', message=word, app_name='Virtual Assistant')
        sleep(1)
        Speak(word)
        stand_by()
        Speak(get_word("after_stand_by"))


def Speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


if __name__ == '__main__':
    main()
