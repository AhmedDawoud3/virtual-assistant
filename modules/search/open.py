import json
import os
import webbrowser as wb
import subprocess
from getpass import getuser


class Open:
    def search(text):
        if "internet" in text or "browser" in text:
            wb.open_new_tab('http://www.google.com')
            return "Opening..."
        else:
            if Open.search_apps(text):
                return f"Opening {text}..."

            if Open.search_websites(text):
                return f"Opening {text}..."

            wb.open_new_tab(f'https://www.google.com/search?q={text}')
            return "There is some results from the web"

    def search_apps(text):
        with open(os.path.join("data", "apps.json"), "r") as f:
            data = json.loads(f.read())
            for app in data:
                if text in app:
                    app = data[app]
                    process = subprocess.Popen(
                        ['start', '', app.replace("username", getuser())], shell=True)
                    process.wait()
                    return True
        return False

    def search_websites(text):
        with open(os.path.join("data", "websites.json"), "r") as f:
            data = json.loads(f.read())
            for site in data:
                if text in site:
                    site = data[site]
                    wb.open_new_tab(site)
                    return True
        return False
