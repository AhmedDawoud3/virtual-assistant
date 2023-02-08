import json
import requests
from datetime import datetime
from time import strftime


def Prayer(city):
    url = "https://aladhan.p.rapidapi.com/timingsByCity"
    querystring = {"city": city, "country": "Egypt"}
    headers = {
        'x-rapidapi-key': "8e75703283mshfe1e00b6a64bd86p120da7jsn679533d8c30f",
        'x-rapidapi-host': "aladhan.p.rapidapi.com"
    }

    try:
        response = requests.request(
            "GET", url, headers=headers, params=querystring)
    except requests.exceptions.ConnectionError:
        return "Sorry, couldn't get prayer times. Please, check your Internet Connection"

    data = json.loads(response.text)
    prayer = data['data']['timings']
    timestamp2 = strftime('%H:%M')

    for pray in prayer:
        if pray in ["Fajr", "Dhuhr", "Asr", "Maghrib", "Isha"]:
            t1 = datetime.strptime(timestamp2, "%H:%M")
            t2 = datetime.strptime(prayer[pray], "%H:%M")

            difference = str(t2 - t1)

            if "-" not in difference:
                if difference[1] != ":":
                    return f"{int(difference[:2])} hours {int(difference[3:5])} minutes left for Al {str(pray)}"

                if difference[0] == "0":
                    return f"{int(difference[2:4])} minutes left for Al {str(pray)}"
                else:
                    return f"{int(difference[0])} hours {int(difference[2:4])} minutes left for Al {str(pray)}"
                
    t1 = datetime.strptime(timestamp2, "%H:%M")
    t2 = datetime.strptime(prayer["Fajr"], "%H:%M")

    difference = t2 - t1

    if len(str(difference)) == 16:
        hours = int(str(difference)[8:10])
        minutes = int(str(difference)[11:13])
    else:
        hours = int(str(difference)[8:9])
        minutes = int(str(difference)[10:12])

    return f"{hours} hours {minutes} minutes left for Al Fajr"
