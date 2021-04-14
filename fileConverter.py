import subprocess

from pyttsx3 import speak
import app
import os.path
from os import path


def convertFile():
    app.speakPrint('Please write down the "path" of the -original- file')
    app.speakPrint(
        'You can click "shift + right-click" and choose copy as path')
    src = input()
    src = src.replace("\\", "\\\\").replace('"', "")
    while True:
        if not path.exists(src):
            app.speakPrint(
                "Sorry, Didn't find the file\nMake Sure To write the path correctly")
            src = input()
            src = src.replace("\\", "\\\\")
        else:
            break

    app.speakPrint(
        'Please write down the name of the new file followed by the extension')
    print('Ex. : output.mp3')
    dst = input()
    while True:
        if src[0] == " ":
            src = src[1:]
        else:
            break
    if path.exists('Converted Files') == False:
        os.mkdir("Converted Files")
        app.speakPrint(
            '"Converted Files" folder has successfully been created')

    app.Speak("Converting")
    subprocess.call(['Utils\\ffmpeg.exe', '-i',
                    src, f'Converted Files/{dst}'])
    speak("Done")
