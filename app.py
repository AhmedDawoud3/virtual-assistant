import speech_recognition as sr
import pyttsx3
import sqlite3
import os
from calc import *
import subprocess
from open_apps import openApp


r = sr.Recognizer()

engine = pyttsx3.init()

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main():
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

                if "+" in MyText or "-" in MyText or "*" in MyText or "/" in MyText:
                    try:
                        result = eval(MyText)
                        Speak(f"The answer is {result}")
                        print(f"The answer is {result}")
                    except:
                        Speak("What was That ?")

                # Open Programmes
                elif "open" in MyText:
                    MyText = MyText.replace("open ", "")
                    openApp(MyText)

                # Google Search
                # else

                elif "bye" in MyText:
                    quit()

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")


def Speak(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()


if __name__ == '__main__':
    main()
