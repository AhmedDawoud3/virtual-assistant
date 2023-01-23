from modules.model import Model
import speech_recognition as sr
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

        # Start speech recognition module
        self.recognise = sr.Recognizer()

        # make sure that GUI has been initialized
        while not self.gui.is_ready:
            continue

        # Check user data
        model.check_user_data(self. _in, self._out, self.engine, self.v)

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
            # Wait for speech command
            if keyboard.is_pressed('alt + v'):
                with sr.Microphone() as source2:
                    # Get command from Microphone
                    try:
                        self.say(get_word("after_stand_by"))
                        print("Adjusting Audio")
                        self.recognise.adjust_for_ambient_noise(
                            source2, duration=0.2)
                        print("Listening")
                        audio2 = self.recognise.listen(source2)
                        print("Processing The Data ")
                        text = self.recognise.recognize_google(audio2)
                    except sr.RequestError as e:
                        self._out("Could not request results; {0}".format(e))
                        continue

                    except sr.UnknownValueError:
                        self._out("unknown error occured")
                        continue

                    # Send command to GUI
                    self.gui.gui_in(text)
                    self.gui.clear_entry()
                    return text

            if keyboard.is_pressed('enter') and self.gui.gui_get_text() != "" and self.gui.is_focused():
                # Get command from Entry field
                text = self.gui.gui_get_text()

                # Send command to GUI
                self.gui.gui_in(text)
                self.gui.clear_entry()
                return text

    # Control app output
    def _out(self, text, silent=False):
        print(text)
        self.gui.gui_out(text)
        if not silent:
            self.say(text)

    def say(self, text):
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
