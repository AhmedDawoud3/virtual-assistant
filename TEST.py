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
import webbrowser as wb
wb.open_new_tab('http://www.google.com')
