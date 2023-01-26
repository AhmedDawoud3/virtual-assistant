import json
import os

from geopy.geocoders import Nominatim


class UserData:
    def __init__(self):
        self.path = os.path.join("data", "user.json")
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.data = json.loads(f.read())
        else:
            self.data = {
                'username': "",
                'city': '',
                'voice': 1,
                'theme': 0
            }

    def update_data_file(self):
        with open(self.path, "w") as f:
            f.write(json.dumps(self.data))

    def get_name(self):
        return self.data['username']

    def get_city(self):
        return self.data['city']

    def get_voice(self):
        return self.data['voice']

    def get_theme(self):
        return self.data['theme']

    def set_name(self, name):
        self.data['username'] = name
        self.update_data_file()

    def set_city(self, city):
        self.data['city'] = city
        self.update_data_file()

    def set_voice(self, voice):
        self.data['voice'] = voice
        self.update_data_file()

    def set_theme(self, theme):
        self.data['theme'] = theme
        self.update_data_file()

    # For External use in model
    def change_name(self, _in, _out):
        _out("What's your name?")
        name = _in("")
        self.set_name(name)

    def change_city(self, _in, _out):
        while True:
            _out("Please Enter Your City :")
            city = _in("")
            geolocator = Nominatim(user_agent='myapplication')
            location = geolocator.geocode(city)
            if location != None:
                break
        self.set_city(city)

    def change_voice(self, _in, _out, engine, v):
        for a in range(len(v)):
            engine.setProperty('voice', (v[a]))
            _out(f"For this voice press {a}")
        c = _in("Please Choose (0, 1) :")

        while (c != "0" and c != "1"):
            c = _in("Please Choose (0, 1) :")

        c = int(c)
        self.set_voice(c)
        engine.setProperty('voice', v[int(self.get_voice())])
