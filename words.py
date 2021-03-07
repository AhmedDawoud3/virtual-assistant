import random

standBy = [
    "standing by",
    "waiting for your commands",
    "waiting for you",
    "waiting"
]

runAfterStandBy = [
    "I'm still here",
    "Didn't go",
    "at your service"
]


artists = ["Jazz", "Rapp", "Classic", "Rock"]


def get_word(keyword):
    if keyword == "stand_by":
        return random.choice(standBy)
    elif keyword == "after_stand_by":
        return random.choice(runAfterStandBy)
    elif keyword == "artist":
        return random.choice(artists)
