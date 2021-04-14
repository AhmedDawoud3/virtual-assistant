# from plyer import notification
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
import youtube_downloader
from math import *
from azan import *
from voice_activation import *
from words import get_word
from app_closer import closeApp
from pyttsx3.drivers import sapi5
import random
from music_player import *
import fileConverter
from os import path

version = 0.1

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
    music = None
    music_list = []
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

    if not path.exists('Utils\\ffmpeg.exe'):
        print("Please Make Sure To Download The Utils (FFMPEG.exe was not found)")
        Speak(
            "Please Make Sure To Download The Utils (F F M P E G dot exe was not found)")
        sleep(10)
        return False

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
                    Speak("Checking Weather")
                    Speak(
                        f"The weather in {city} is {weather_message()[0]}  degrees ,  and {weather_message()[1]}")

                elif "date" in MyText:
                    Speak("Today is " + str(strftime('%A')) + str(int(strftime('%d'))) +
                          str(strftime('%B')) + str(strftime('%Y')))

                elif "azan" in MyText or "pray" in MyText:
                    Speak(get_prayer(city))

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

                elif "what is" in MyText or "what's" in MyText:
                    search = MyText.replace("what is ", "")
                    try:
                        print(wikipedia.summary(search))
                        Speak("According to wikipedia " +
                              str(wikipedia.summary(search, sentences=4)))
                    except:
                        search = MyText.replace(
                            "what is ", "")
                        wb.open_new_tab(
                            f'https://www.google.com/search?q={search}')

                elif "who is" in MyText:
                    search = MyText.replace("who is ", "")
                    try:
                        print(wikipedia.summary(search))
                        Speak("According to wikipedia " +
                              str(wikipedia.summary(search, sentences=4)))
                    except:
                        search = MyText.replace(
                            "who is ", "")
                        wb.open_new_tab(
                            f'https://www.google.com/search?q={search}')

                # Download From Youtube
                elif "download" in MyText:
                    if 'music' in MyText:
                        url = speakInput(
                            "Please write down the name of the song you want to download :")
                        youtube_downloader.youtube_download(url, "music")
                    elif "youtube" in MyText:
                        url = speakInput(
                            "Please type the name of the video you want to download :")
                        youtube_downloader.youtube_download(url, "youtube")

                elif "convert" in MyText:
                    fileConverter.convertFile()

                # Music Player
                elif "music" in MyText:
                    if "play" in MyText:
                        artist = MyText.replace("play music ", "")
                        if artist == "play music":
                            artist = get_word("artist")

                        Speak(f"Playing {artist} Music")
                        music, music_list = music_player(artist, music)

                    elif "pause" in MyText or "stop" in MyText or "continue" in MyText:
                        pause_music(music)

                    elif "next" in MyText:
                        if music == None:
                            artist = get_word("artist") + " music"
                            music, music_list = music_player(artist, music)
                        else:
                            Speak("Playing next music")
                            music = next_music(music, music_list)

                # Brightness Control
                elif "brightness" in MyText:
                    old = sbc.get_brightness()
                    if "increase" in MyText or "raise" in MyText:
                        sbc.set_brightness(old + 25)
                        speakPrint(f"increasing brightness")
                    elif "max" in MyText:
                        sbc.set_brightness(100)
                        speakPrint(f"maximum brightness")
                    elif "decrease" in MyText or "lower" in MyText:
                        speakPrint(f"decreasing brightness")
                        sbc.set_brightness(old - 25)
                    elif "min" in MyText:
                        speakPrint(f"Mnimun brightness")
                        sbc.set_brightness(0)
                    else:
                        speakPrint(f"Current brightness is {old}")

                elif "close" in MyText:
                    MyText = MyText.replace("close ", "")
                    Speak(f"Closing {MyText}")
                    x = closeApp(MyText)
                    if not x:
                        speakPrint(
                            f"Nothing found, Please Make Sure That the name is the same in The Task Manager")
                    else:
                        speakPrint(f"{x} Closed")

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
                elif "bye" in MyText or "quit" in MyText or "leave" in MyText or "stop" in MyText or "adios" in MyText:
                    Speak("it was an honor serving here ")
                    quit()

        except sr.RequestError as e:
            speakPrint("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            speakPrint("unknown error occured")

        word = get_word("stand_by")
        sleep(1)
        Speak(word)
        stand_by()
        Speak(get_word("after_stand_by"))


def Speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


def speakPrint(string):
    Speak(string)
    print(string)


def speakInput(string):
    Speak(string)
    x = input(string)
    return x


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


if __name__ == '__main__':
    main()
