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


class Model:
    def __init__(self):
        data = UserData()
        self.name = data.get_name()
        self.city = data.get_city()

    def process(self, text):
        text = text.lower()

        calc = Calculate()
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

        # elif "download" in text:
        #     text = text.replace("download ", "")
        #     download = Download()
        #     if "youtube" in text:
        #         text = text.replace("youtube", "")
        #         if download.youtube_search():
        #             download.youtube_download()
        #     elif "music" in text:
        #         text = text.replace("music", "")

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
        return (False, "Sorry I didn't understand")
