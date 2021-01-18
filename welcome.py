from time import gmtime, strftime
import geocoder
import requests
from geopy.geocoders import Nominatim
import json
hour_now = int(strftime("%H"))


def welcome_mesage():
    if hour_now >= 6 and hour_now <= 11:
        return "Morning"
    elif hour_now >= 12 and hour_now <= 17:
        return "afternoon"
    elif hour_now >= 18 and hour_now <= 23:
        return "evening"
    else:
        return "night"


def weather_message():
    data = json.load(open('user.json',))
    city = data["city"]
    geolocator = Nominatim(user_agent='myapplication')
    lat = str(geolocator.geocode(city).raw["lat"])
    lon = str(geolocator.geocode(city).raw["lon"])

    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(lon) + "&lon=" + str(lat)
    data = requests.get(api_url)
    data_json = data.json()
    if data_json['cod'] == 200:
        main = data_json['main']
        wind = data_json['wind']
        weather_desc = data_json['weather'][0]
        return [str(main['temp']),  weather_desc['main']]
    else:
        weather_message()
