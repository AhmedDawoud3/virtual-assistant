# import os
# import difflib
# import re
# program = "Office"
# os.chdir("C://Program Files")

# apps = os.listdir()
# for app in apps:
#     if re.match(f".*{program}.*", app):
#         print(app)

# # print(difflib.get_close_matches(program, apps, n=1))


# # importing the module
# import subprocess

# # traverse the software list
# Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
# a = str(Data)

# # try block
# try:

#     # arrange the string
#     for i in range(len(a)):
#         print(a.split("\\r\\r\\n")[6:][i])

# except IndexError as e:
#     print("All Done")

# import modules

# import os
# # os.system('cmd')

# # os.system('start zoom')


# import webbrowser
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# webbrowser.get(chrome_path).open('http://docs.python.org/')
# import webbrowser as wb
# wb.open_new_tab('http://www.google.com')

# from getpass import getuser
# # print(getuser())

# import subprocess
# # print(os.getenv('username'))

# # x = os.path.join("C:\\Users", "Ahmed^ Dawoud",
# #                 "AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
# # os.system(f"start {x}")

# subprocess.Popen(
#     ['start', '', "C:\\Users\\Ahmed Dawoud\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"], shell=True)

# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent='myapplication')
# location = geolocator.geocode("ss")
# print(location.raw)


# import json

# with open("user.json", 'r+') as f:
#     data = json.load(f)
#     data['id'] = 134  # <--- add `id` value.
#     f.seek(0)        # <--- should reset file position to the beginning.
#     json.dump(data, f, indent=4)
#     f.truncate()     # remove remaining part
# from youtube_search import YoutubeSearch

# results = YoutubeSearch('Hello', max_results=10).to_json()

# print(results)

# # returns a json string

########################################

# results = YoutubeSearch('search terms', max_results=10).to_dict()

# print(results)
# # returns a dictionary

# import keyboard
# keyboard.press_and_release('next')
# import keyboard

# keyboard.wait("w")
# print("Hello world!")

# import json
# import requests
# from time import sleep
# from datetime import datetime
# from time import *

# url = "https://aladhan.p.rapidapi.com/timingsByCity"

# querystring = {"city": "kafr el sheikh", "country": "Egypt"}

# headers = {
#     'x-rapidapi-key': "8e75703283mshfe1e00b6a64bd86p120da7jsn679533d8c30f",
#     'x-rapidapi-host': "aladhan.p.rapidapi.com"
# }

# response = requests.request(
#     "GET", url, headers=headers, params=querystring)

# data = json.loads(response.text)

# prayer = data['data']['timings']
# print(f'Fajr at {Fajr}')
# print(f'Sunrise at {Sunrise}')
# print(f'Dhuhr at {Dhuhr}')
# print(f'Asr at {Asr}')
# print(f'Sunset at {Sunset}')
# print(f'Maghrib at {Maghrib}')
# print(f'Isha at {Isha}')
# print(f'Imsak at {Imsak}')
# print(f'Midnight at {Midnight}')

# print()
# timestamp2 = strftime('%H:%M')
# timestamp1 = "15:48"
# found = False
# for pray in prayer:
#     if pray in ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]:
#         t1 = datetime.strptime(timestamp2, "%H:%M")
#         t2 = datetime.strptime(prayer[pray], "%H:%M")

#         difference = str(t2 - t1)

#         if "-" not in difference:
#             found = True
#             print(str(pray) + difference)

# if found == False:
#     t1 = datetime.strptime(timestamp2, "%H:%M")
#     t2 = datetime.strptime(prayer["Fajr"], "%H:%M")

#     difference = t2 - t1

#     print(str(difference)[8:10] + " hours " +
#           str(difference)[11:13] + " minutes lef for Al Fajr")


# latest = max((t1, t2))  # t1, in this case
# print(latest)


# from plyer import notification
# import time
# import screen_brightness_control as sbc


# # 20 minutes = 1200 seconds

# def main():
#     # Start the first notification
#     notification.notify(
#         title='Started',
#         message='Eye comforter has benn started',
#         app_name='Eye Comfort'
#     )
#     time.sleep(1)
#     while True:
#         try:
#             # Wait 20 minutes before sending a notification {Feel free to chnage it}
#             time.sleep(1200)
#             # Getting the old value for the brightness
#             old = sbc.get_brightness()
#             # Decreasing the brightness to half its original value
#             sbc.set_brightness(old/2)
#             print("!!")
#             # Display the notification
#             notification.notify(
#                 title='Take a break',
#                 message='Look away from the monitor for 20 seconds',
#                 app_name='Eye Comfort'
#             )
#             # Wait for 20 seconds before setting the brightness to its original value
#             time.sleep(20)
#             sbc.set_brightness(old)
#             print("!")
#             notification.notify(
#                 title='Take a break',
#                 message='Look away from the monitor for 20 seconds',
#                 app_name='Eye Comfort'
#             )
#         except KeyboardInterrupt:
#             print("Closed")
#             break


# if __name__ == '__main__':
#     main()

# import wmi
# import os
# import re
# import subprocess
# # Initializing the wmi constructor
# f = wmi.WMI()

# # Printing the header for the later columns
# p = "chrome"
# # Iterating through all the running processes
# for process in f.Win32_Process():
#     if re.match(f".*{p}.*", str(process.Name).replace(".exe", "")):
#         # Displaying the P_ID and P_Name of the process
#         # print(f"{process.ProcessId:<10} {process.Name}")

#         try:
#             # sys.stdout = open(os.devnull, 'w')
#             # os.system(f"TASKKILL /F /IM {process.Name}")

#             subprocess.call(
#                 ["taskkill", "/F", "/IM", process.Name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
#         except:
#             break


# import time

# begin = time.time()

# # program body starts

# # for i in range(5):
# #     print("GeeksForGeeks")
# # program body ends
# # store end time
# while True:
#     end = time.time()
#     if(end - begin) >= 2:
#         print("hello")
#         begin = time.time()
# total time taken
# print(f"Total runtime of the program is {end - begin}")

# import pyttsx3
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty(
#     'voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
# engine.say("Hello World!")
# engine.runAndWait()
# engine.stop()

# from pydub import AudioSegment

# song = AudioSegment.from_file("music\Snowman.webm", "webm")
# print("Loaded")
# song.export("neco.mp3", format="mp3", bitrate="320k")
# print("Converted and saved")

# from audioplayer import AudioPlayer
# import time

# # Playback stops when the object is destroyed (GC'ed), so save a reference to the object for non-blocking playback.
# AudioPlayer("music\Snowman.m4a").play(block=True)
# # time.sleep(5)
# AudioPlayer("E:\Projects\Python\youtube-dl\Abandoned & Shiah Maisel - Finally Healing [NCS Release].m4a").stop()


# import vlc
# import time

# # creating vlc media player object
# media = vlc.MediaPlayer("music\Snowman.m4a")

# # start playing video
# media.play()
# time.sleep(5)

import vlc
import time

# importing pafy module
import pafy

# url of the video
url = "https://www.youtube.com/watch?v=loB4bRVTVbA"

# creating pafy object of the video
video = pafy.new(url)

# getting stream at index 0
best = video.streams[0]

# creating vlc media player object
media = vlc.MediaPlayer(video.allstreams[1].url)

# start playing video
media.play()
time.sleep(5)
