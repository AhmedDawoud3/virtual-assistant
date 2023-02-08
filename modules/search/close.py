import wmi
import subprocess
f = wmi.WMI()


class Close:
    @classmethod
    def search(cls, text: str) -> bool:
        for process in f.Win32_Process():
            if text in str(process.Name):
                subprocess.call(
                    ["taskkill", "/F", "/IM", process.Name], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                return True

        return False
