import wmi
import re
import subprocess
f = wmi.WMI()


def closeApp(p):
    for process in f.Win32_Process():
        if p in str(process.Name).replace(".exe", ""):
            subprocess.call(
                ["taskkill", "/F", "/IM", process.Name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            return process.Name
