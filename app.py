from modules.model import Model
import json
import pyttsx3
from funcs import *


class Main():
    def __init__(self):
        self.v = ["HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0",
                  "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"]

        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', self.v[0])

    def main(self):
        model = Model()

        # Check user data
        model.check_user_data(self. _in, self._out, self.engine, self.v)

        # Welcome message
        self._out(f"Good {welcome_mesage()} {model.name}")
        self._out(model.process("get time")[1])

        # Start Main loop
        while True:
            command = self._in("Enter your command: ")
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

    def _in(self, text):
        # self.engine.say(text)
        # self.engine.runAndWait()
        return input(text)

    def _out(self, text):
        print(text)
        self.engine.say(text)
        self.engine.runAndWait()


if __name__ == "__main__":
    main = Main()
    main.main()
