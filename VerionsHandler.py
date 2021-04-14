import requests


def GetLatestVersion():
    response = requests.get(
        'https://thevirtualassistant.netlify.app/latestversion')
    version = str(response.content)
    verison = float(version.replace(
        "b'<!DOCTYPE html>\\n\\n<html>\\n  <body>\\n    ", "").replace("\\n  </body>\\n</html>\\n'", ""))
    return(verison)


def CheckUpdate(currentVersion):
    if currentVersion < GetLatestVersion():
        return True
    return False
