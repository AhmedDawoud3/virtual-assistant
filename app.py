from modules.model import Model
import json
import pyttsx3
from funcs import *
from gui import GUI
import threading
import keyboard


class Main():
    def __init__(self):
        self.v = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
                  "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"]

        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.v[0])

    def main(self):
        model = Model()

        # Start initializing GUI
        self.gui = GUI()

        gui = threading.Thread(target=self.gui.init)
        gui.daemon = True
        gui.start()

        # Check user data
        model.check_user_data(self. _in, self._out, self.engine, self.v)

        # make sure that GUI has been initialized
        while not self.gui.is_ready:
            continue

        # Welcome message
        self._out(f"Good {welcome_mesage()} {model.name}")
        self._out(model.process("get time")[1])

        # Start Main loop
        while True:
            command = self._in("")
            respond = model.process(command)

            # A response of one message
            if respond[0] == True:
                self._out(respond[1])

            # A response that call a function for direct conversation
            elif respond[0] == False:
                respond[1](self._in, self._out)

            # A response that call for audio engine to change the voice
            elif respond[0] == 4001:
                respond[1](self._in, self._out, self.engine, self.v)

            # A response that call for exit function to safety exit
            elif respond[0] == 4002:
                respond[1](self._in, self._out, self.app_exit)

    # def _in(self, text):
    #     # self.engine.say(text)
    #     # self.engine.runAndWait()
    #     # return input(text)
    #     text = input(text)
    #     # self.gui.gui_in(text)
    #     return text

    # Control user Input
    def _in(self, text):
        # Show a message with the request
        if text != "":
            self._out(text)

        # wait for Enter key press
        while True:
            print("looping")
            try:
                if keyboard.is_pressed('enter') and self.gui.gui_get_text() != "":
                    text = self.gui.gui_get_text()
                    self.gui.gui_in(text)
                    self.gui.clear_entry()
                    return text
            except:
                break

    # Control app output
    def _out(self, text, silent=False):
        print(text)
        self.gui.gui_out(text)
        if not silent:
            self.engine.say(text)
            self.engine.runAndWait()

    # Safely exit the app
    def app_exit(self):
        # self.gui.gui_destroy()
        # print("Destroyed from App")
        quit()


if __name__ == "__main__":
    main = Main()
    main.main()
