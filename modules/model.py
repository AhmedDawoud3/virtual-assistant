from funcs import *
from time import strftime

from modules.calculate.calculate import Calculate
from modules.user_data.user_data import UserData
from modules.weather.weather import Weather
from modules.prayer.prayer import Prayer
from modules.notes.notes import Notes
from modules.search.open import Open
from modules.search.wiki import Wiki
from modules.search.close import Close
from modules.search.update import Update
from modules.download.download import Download
from modules.media.music import Music
from modules.system.brightness import Brightness
from modules.system.shutdown import Shutdown
from modules.system.restart import Restart
from modules.system.convert import Convert


class Model:
    def __init__(self):
        self.data = UserData()
        self.name = self.data.get_name()
        self.city = self.data.get_city()
        self.voice = self.data.get_voice()

        self.music = Music()
        self.update = Update()
        self.notes = Notes()

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

        elif "note" in text:
            # if "show" in text or "get" in text or "open" in text:
            #     return (False, self.notes.show_notes)

            if "add" in text or "take" in text or "make" in text:
                return (False, self.notes.va_add_note)

            elif "edit" in text or "change" in text:
                return (False, self.notes.va_edit_note)

            elif "delete" in text or "remove" in text:
                return (False, self.notes.va_delete_note)

            else:
                return (False, self.notes.va_show_notes)

        elif "open" in text:
            text = text.replace("open ", "")
            return (True, Open.search(text))

        elif "what is" in text or "what's" in text or "who is" in text or "who's" in text:
            return self.handle_wh_questoin(text)

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

        elif "convert" in text:
            return (False, Convert.convert)

        elif "music" in text:
            if "play" in text:
                text = text.replace("music", "").replace("play", "").strip()
                if text == "":
                    # Continue music in queue
                    if self.music.music != None and not self.music.is_playing():
                        self.music.pause_continue()
                        return (True, "Playing music...")

                    if self.music != None and self.music.is_playing():
                        return (True, "Music is already playing")

                    # Start music with random artist
                    text = get_word("artist")
                self.music.search_and_play(text)
                return (True, f"Playing {text} music...")

            elif "pause" in text or "stop" in text:
                if self.music.music is None or not self.music.is_playing():
                    return (True, "Music is not playing")
                self.music.pause_continue()

                return (True, "Pausing music..." if "pause" in text else "Stopping music...")
            
            elif "continue" in text:
                if self.music.music is None:
                    self.music.search_and_play(get_word("artist"))
                    return (True, "Playing music...")
                else:
                    if self.music.is_playing():
                        return (True, "Music is already playing")

                    self.music.pause_continue()
                    return (True, "Continuing music...")

            elif "next" in text:
                if self.music.music is None:
                    self.music.search_and_play(get_word("artist"))
                else:
                    self.music.next()
                return (True, "Playing next music...")

            elif "prev" in text:
                if self.music.music is None:
                    self.music.search_and_play(get_word("artist"))
                else:
                    self.music.prev()
                return (True, "Playing previous music...")

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

        elif "check" in text and "update" in text:
            if self.update.check():
                return (True, "There's an available update")
            else:
                return (True, "You Are Running The Latest Version")

        elif "help" in text:
            Open.search("virtual assistant")
            return (True, "Check our website for help")

        elif "shutdown" in text or "shut down" in text:
            shutdown = Shutdown()
            return shutdown.shutdown(text)

        elif "restart" in text:
            restart = Restart()
            return restart.restart(text)

        elif "bye" in text or "quit" in text or "leave" in text or "stop" in text or "adios" in text:
            return (4002, self.model_exit_msg)

        return (True, "Sorry I didn't understand")

    def handle_wh_questoin(self, text):
        text = text.replace("what is ", "")
        text = text.replace("what's ", "")
        text = text.replace("who is ", "")
        text = text.replace("who's ", "")

        wiki = Wiki()
        return (
            (True, wiki.get_result())
            if wiki.wiki_search(text)
            else (True, "This is some results from the web")
        )

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

    def get_theme(self):
        return self.data.get_theme()

    def set_theme(self, i):
        self.data.set_theme(i)

    def model_exit_msg(self, _in, _out, app_exit):
        self.music.stop()
        _out("It was an honor serving here")
        app_exit()
