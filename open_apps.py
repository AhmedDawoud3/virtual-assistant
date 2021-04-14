import json
import re
import os
import webbrowser as wb
import subprocess
from getpass import getuser

username = getuser()


def openApp(MyText):
    MyText = MyText
    if "internet" in MyText or "browser" in MyText:
        wb.open_new_tab('http://www.google.com')
    else:
        f = open('Data\\apps.json',)

        data = json.load(f)

        for app in data:
            # print(f"{app} : {data[app]}")
            if MyText in app:
                app = data[app]
                app = app.replace("username", username)
                # os.system(f"start /c {data[app]}")
                subprocess.Popen(
                    ['start', '', app], shell=True)
                f.close()
                return True

        f.close()

        f = open('Data\\websites.json',)

        data = json.load(f)

        for site in data:
            if MyText in site:
                site = data[site]
                wb.open_new_tab(site)
                f.close()
                return True
        f.close()
        wb.open_new_tab(f'https://www.google.com/search?q={MyText}')
        return False
