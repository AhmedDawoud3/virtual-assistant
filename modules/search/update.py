import requests
import webbrowser as wb
from time import sleep


class Update:
    def __init__(self):
        self.current_version = 0.3

    def check(self):
        if self.get_current_version() < self.get_latest_version():
            wb.open_new_tab(
                'https://thevirtualassistant.netlify.app/')
            return True
        return False

    def get_latest_version(self):
        while True:
            try:
                response = requests.get(
                    'https://thevirtualassistant.netlify.app/latestversion')
                version = str(response.content)
                version = float(version.replace(
                    "b'<!DOCTYPE html>\\n\\n<html>\\n  <body>\\n    ", "").replace("\\n  </body>\\n</html>\\n'", ""))
            except requests.exceptions.ConnectionError:
                sleep(1)
                print("Server connection error")
                continue
            break
        print(f"Latest version: {version}")
        return version

    def get_current_version(self):
        print(f"Current version: {self.current_version}")
        return self.current_version
