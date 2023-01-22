from time import strftime

from modules.calculate.calculate import Calculate
from modules.user_data.user_data import UserData
from modules.weather.weather import Weather
from modules.prayer.prayer import Prayer
from modules.search.open import Open
from modules.search.wiki import Wiki
from modules.search.close import Close
from modules.download.download import Download
from modules.system.brightness import Brightness
from modules.system.shutdown import Shutdown
from modules.system.restart import Restart
import json


class Model:
    def __init__(self):
        self.data = UserData()
        self.name = self.data.get_name()
        self.city = self.data.get_city()
        self.voice = self.data.get_voice()

    def process(self, text):
        text = text.lower()

        calc = Calculate()

        if "hello" in text:
            return (True, "Hello to you too!")
        if calc.can_calculate(text):
            return (True, calc.get_result())

        elif "weather" in text:
            return (True, Weather(self.city))

        elif "date" in text and "update" not in text:
            return (True, f"Today is {strftime('%A')} {int(strftime('%d'))} {strftime('%B')} {strftime('%Y')}")

        elif "time" in text:
            return (True, f"It's {int(strftime('%I'))} {int(strftime('%M'))} {strftime('%p')}")

        elif "pray" in text or "azan" in text:
            return (True, Prayer(self.city))

        elif "change" in text and "name" in text:
            return (False, self.data.change_name)

        elif "change" in text and "city" in text:
            return (False, self.data.change_city)

        elif "change" in text and "voice" in text:
            return (4001, self.data.change_voice)

        elif "open" in text:
            text = text.replace("open ", "")
            return (True, Open.search(text))

        elif "what is" in text or "what's" in text or "who is" in text or "who's" in text:
            text = text.replace("what is ", "")
            text = text.replace("what's ", "")
            text = text.replace("who is ", "")
            text = text.replace("who's ", "")

            wiki = Wiki()
            if wiki.wiki_search(text):
                return (True, wiki.get_result())
            else:
                return (True, "This is some results from the web")

        elif "google" in text:
            text = text.replace("google ", "")
            Wiki.google_search(text)
            return (True, "This is some results from the web")

        elif "download" in text:
            text = text.replace("download ", "")
            download = Download()
            if "youtube" in text:
                return (False, download.youtube_download)
            elif "music" in text:
                return (False, download.music_download)

        elif "brightness" in text:
            brightness = Brightness()
            if "increase" in text or "raise" in text:
                return (True, brightness.increase())

            elif "decrease" in text or "lower" in text:
                return (True, brightness.decrease())

            elif "max" in text:
                return (True, brightness.maximum())

            elif "min" in text:
                return (True, brightness.minimum())

            else:
                return (True, f"Current brightness is {brightness.get_current_value()}")

        elif "close" in text:
            text = text.replace("close ", "")
            if Close.search(text):
                return (True, f"Closing {text}")
            # return (True, Close.search(text))

        elif "shutdown" in text or "shut down" in text:
            shutdown = Shutdown()
            return shutdown.shutdown(text)

        elif "restart" in text:
            restart = Restart()
            return restart.restart(text)
        return (True, "Sorry I didn't understand")

    def check_user_data(self, _in, _out, engine, v):
        # Check the username
        if self.name == "":
            _out("Hello I'm your virtual assistant.")
            self.data.change_name(_in, _out)
            self.name = self.data.get_name()

        # Check the city
        if self.city == "":
            self.data.change_city(_in, _out)
            self.city = self.data.get_city()

        # Check the voice
        if self.voice == "":
            self.data.change_voice(_in, _out, engine, v)
            self.voice = self.data.get_voice()
