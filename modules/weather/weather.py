import requests
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable


def Weather(city):
    geolocator = Nominatim(user_agent='myapplication')
    try:
        lat = str(geolocator.geocode(city).raw["lat"])
        lon = str(geolocator.geocode(city).raw["lon"])
    except AttributeError:
        return "Sorry, Couldn't get weather"
    except GeocoderUnavailable:
        return "Sorry, Couldn't get weather. Please, check your Internet connection"

    api_url = "https://fcc-weather-api.glitch.me/api/current?lat=" + \
        str(lon) + "&lon=" + str(lat)
    data = requests.get(api_url)
    data_json = data.json()

    if data_json['cod'] == 200:
        main = data_json['main']
        weather_desc = data_json['weather'][0]
        return f"The weather in {city} is {main['temp']}  degrees ,  and { weather_desc['main']}"
    else:
        Weather(city)
