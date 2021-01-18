# import os
# import difflib
# import re
# program = "Office"
# os.chdir("C://Program Files")

# apps = os.listdir()
# for app in apps:
#     if re.match(f".*{program}.*", app):
#         print(app)

# # print(difflib.get_close_matches(program, apps, n=1))


# # importing the module
# import subprocess

# # traverse the software list
# Data = subprocess.check_output(['wmic', 'product', 'get', 'name'])
# a = str(Data)

# # try block
# try:

#     # arrange the string
#     for i in range(len(a)):
#         print(a.split("\\r\\r\\n")[6:][i])

# except IndexError as e:
#     print("All Done")

# import modules

# import os
# # os.system('cmd')

# # os.system('start zoom')


# import webbrowser
# chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# webbrowser.get(chrome_path).open('http://docs.python.org/')
# import webbrowser as wb
# wb.open_new_tab('http://www.google.com')

# from getpass import getuser
# # print(getuser())

# import subprocess
# # print(os.getenv('username'))

# # x = os.path.join("C:\\Users", "Ahmed^ Dawoud",
# #                 "AppData\\Roaming\\Zoom\\bin\\Zoom.exe")
# # os.system(f"start {x}")

# subprocess.Popen(
#     ['start', '', "C:\\Users\\Ahmed Dawoud\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"], shell=True)

# from geopy.geocoders import Nominatim
# geolocator = Nominatim(user_agent='myapplication')
# location = geolocator.geocode("ss")
# print(location.raw)


# import json

# with open("user.json", 'r+') as f:
#     data = json.load(f)
#     data['id'] = 134  # <--- add `id` value.
#     f.seek(0)        # <--- should reset file position to the beginning.
#     json.dump(data, f, indent=4)
#     f.truncate()     # remove remaining part
from youtube_search import YoutubeSearch

results = YoutubeSearch('Hello', max_results=10).to_json()

print(results)

# returns a json string

########################################

# results = YoutubeSearch('search terms', max_results=10).to_dict()

# print(results)
# # returns a dictionary
