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


THEMES = [{
    # "bg": "#1A120B",
    # "app": "#3C2A21",
    # "user": "#D5CEA3",
    # "text": "#E5E5CB"
    "bg": "#2A2438",
    "app": "#352F44",
    "user": "#5C5470",
    "text": "#DBD8E3"
}, {
    "bg": "#F7ECDE",
    "app": "#E9DAC1",
    "user": "#54BAB9",
    "text": "#000"
}, {
    "bg": "#FAF8F1",
    "app": "#FAEAB1",
    "user": "#C58940",
    "text": "#000"
}, {
    "app": "#CEE5D0",
    "bg": "#F3F0D7",
    "user": "#E0C097",
    "text": "#000"
}]


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
