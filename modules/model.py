from time import strftime

from modules.calculate.calculate import Calculate
from modules.user_data.user_data import UserData
from modules.weather.weather import Weather
from modules.prayer.prayer import Prayer
from modules.search.open import Open
from modules.search.wiki import Wiki
from modules.search.close import Close
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
            return calc.get_result()

        elif "weather" in text:
            return Weather(self.city)

        elif "date" in text and "update" not in text:
            return f"Today is {strftime('%A')} {int(strftime('%d'))} {strftime('%B')} {strftime('%Y')}"

        elif "time" in text:
            return f"It's {int(strftime('%I'))} {int(strftime('%M'))} {strftime('%p')}"

        elif "pray" in text or "azan" in text:
            return Prayer(self.city)

        elif "open" in text:
            text = text.replace("open ", "")
            return Open.search(text)

        elif "what is" in text or "what's" in text or "who is" in text or "who's" in text:
            text = text.replace("what is ", "")
            text = text.replace("what's ", "")
            text = text.replace("who is ", "")
            text = text.replace("who's ", "")

            wiki = Wiki()
            return wiki.wiki_search(text)

        elif "google" in text:
            text = text.replace("google ", "")
            return Wiki.google_search(text)

        elif "brightness" in text:
            brightness = Brightness()
            if "increase" in text or "raise" in text:
                return brightness.increase()

            elif "decrease" in text or "lower" in text:
                return brightness.decrease()

            elif "max" in text:
                return brightness.maximum()

            elif "min" in text:
                return brightness.minimum()

            else:
                return brightness.get_current_value()

        elif "close" in text:
            text = text.replace("close ", "")
            return Close.search(text)

        elif "shutdown" in text or "shut down" in text:
            return Shutdown(text)

        elif "restart" in text:
            return Restart(text)
