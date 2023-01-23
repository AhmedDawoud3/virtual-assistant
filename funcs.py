from time import gmtime, strftime
import random
from os import path


hour_now = int(strftime("%H"))

standBy = [
    "standing by",
    "waiting for your commands",
    "waiting for you",
    "waiting"
]

runAfterStandBy = [
    "I'm still here",
    "Didn't go",
    "at your service",
    "alive",
    "here",
    "here we go again",
]


artists = ["Jazz", "Rap", "Classic", "Rock"]


def welcome_mesage():
    if hour_now >= 6 and hour_now <= 11:
        return "Morning"
    elif hour_now >= 12 and hour_now <= 17:
        return "afternoon"
    elif hour_now >= 18 and hour_now <= 23:
        return "evening"
    else:
        return "night"


def get_word(keyword):
    if keyword == "stand_by":
        return random.choice(standBy)
    elif keyword == "after_stand_by":
        return random.choice(runAfterStandBy)
    elif keyword == "artist":
        return random.choice(artists)


def check_ffmpeg():
    if not path.exists('Utils\\ffmpeg.exe'):
        return False
    return True
