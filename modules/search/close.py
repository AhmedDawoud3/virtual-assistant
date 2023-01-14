import wmi
import subprocess
f = wmi.WMI()


class Close:
    def search(text):
        for process in f.Win32_Process():
            if text in str(process.Name):
                subprocess.call(
                    ["taskkill", "/F", "/IM", process.Name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                return True

        return False
