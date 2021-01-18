
import json
import requests
from time import sleep
from datetime import datetime
from time import *


def get_prayer():
    url = "https://aladhan.p.rapidapi.com/timingsByCity"

    querystring = {"city": "kafr el sheikh", "country": "Egypt"}

    headers = {
        'x-rapidapi-key': "8e75703283mshfe1e00b6a64bd86p120da7jsn679533d8c30f",
        'x-rapidapi-host': "aladhan.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)

    prayer = data['data']['timings']

    timestamp2 = strftime('%H:%M')

    found = False
    for pray in prayer:
        if pray in ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]:
            t1 = datetime.strptime(timestamp2, "%H:%M")
            t2 = datetime.strptime(prayer[pray], "%H:%M")

            difference = str(t2 - t1)

            if "-" not in difference:
                found = True
                return f"{int(str(difference)[0:2])} hours {int(str(difference)[3:5])} minutes left for Al {str(pray)}"

    if found == False:
        t1 = datetime.strptime(timestamp2, "%H:%M")
        t2 = datetime.strptime(prayer["Fajr"], "%H:%M")

        difference = t2 - t1

        return f"{int(str(difference)[8:10])} hours {int(str(difference)[11:13])} minutes left for Al Fajr"
