import json
import re
import os
import webbrowser as wb


def openApp(MyText):
    MyText = MyText
    if "internet" in MyText or "browser" in MyText:
        wb.open_new_tab('http://www.google.com')
    else:
        f = open('apps.json',)

        data = json.load(f)

        for app in data:
            # print(f"{app} : {data[app]}")
            if re.match(f".*{MyText}.*", app):
                os.system(f"start {data[app]}")
                f.close()
                quit()
                break
        f.close()
