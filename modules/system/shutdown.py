import os
from time import sleep


class Shutdown:
    def shutdown(self, text):
        if "after" in text or " in " in text:
            time = (self.get_hours(text) * 3600 + self.get_minutes(text) * 60)
            os.system(f"Shutdown -s -t {time}")
            return (True, "Scheduling shutdown")
        else:
            return (False, self.immidiate_shutdown)

    def immidiate_shutdown(self, _in, _out):
        for i in range(11, 0, -1):
            _out(f"Shutting down in {i}")
            sleep(1)
        os.system("shutdown -s")

    def get_hours(self, text):
        hour_found = False
        for i in range(len(text)):
            if str(text[i: i+4]) == "hour":
                hour_found = True
                h = i
                break

        if hour_found:
            for i in range(h, 0, -1):
                if text[i].isdigit():
                    if text[i-1].isdigit():
                        return int(text[i-1: i+1])
                    return int(text[i])
        return 0

    def get_minutes(self, text):
        minute_found = False
        for i in range(len(text)):
            if str(text[i: i+6]) == "minute":
                minute_found = True
                h = i
                break

        if minute_found:
            for i in range(h, 0, -1):
                if text[i].isdigit():
                    if text[i-1].isdigit():
                        if text[i-2].isdigit():
                            return int(text[i-2: i+1])
                        return int(text[i-1: i+1])
                    return int(text[i])
        return 0
