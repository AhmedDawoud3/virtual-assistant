import subprocess
import os
from funcs import *


class Convert:
    def convert(_in, _out):
        if check_ffmpeg():
            _out('Please write down the "path" of the -original- file')
            _out(
                'You can click "shift + right-click" and choose copy as path')
            src = _in("")
            src = src.replace("\\", "\\\\").replace('"', "")
            while True:
                if not os.path.exists(src):
                    _out(
                        "Sorry, Didn't find the file \nMake Sure To write the path correctly")
                    src = _in("")
                    src = src.replace("\\", "\\\\")
                else:
                    break

            _out(
                'Please write down the name of the new file followed by the extension')
            _out('Ex. : output.mp3')
            dst = _in("")
            while True:
                if src[0] == " ":
                    src = src[1:]
                else:
                    break
            if os.path.exists('Converted Files') == False:
                os.mkdir("Converted Files")
                _out(
                    '"Converted Files" folder has successfully been created')

            _out("Converting...")
            subprocess.call(['Utils\\ffmpeg.exe', '-i',
                            src, f'Converted Files/{dst}'])
            _out("Converting have done")
        else:
            _out(
                "Please Make Sure To Download The Utils (FFMPEG.exe was not found)", silent=True)
            _out(
                "Please Make Sure To Download The Utils (F F M P E G dot exe was not found)", write=False)
