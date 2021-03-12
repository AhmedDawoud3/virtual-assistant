from youtube_search import YoutubeSearch
from pafy import new
from app import Speak, speakPrint
import shutil
import os.path
from os import path


def youtube_download(search, dType):

    if dType == "youtube":
        results = YoutubeSearch(search, max_results=1).to_dict()

        url = "https://www.youtube.com" + str(results[0]["url_suffix"])
        video = new(url)

        stream = video.allstreams

        x = 0

        for i in stream:
            print(f"{x} : {i}")
            x += 1

        Speak("Please Choose a quality")
        if path.exists('Downloaded Videos') == False:
            speakPrint(
                "Please Note That\n'audio' is audio only without video,\n'video' is video without audio,\n'normal' is both")
        q = input("Choose quality to download: ")
        if path.exists('Downloaded Videos') == False:
            os.mkdir("Downloaded Videos")
            speakPrint(
                '"Downloaded Videos" folder has successfully been created')

        fileName = str(stream[int(q)].filename)
        Speak("Downloading")
        stream[int(q)].download()
        shutil.move(fileName, f"Downloaded Videos/{fileName}")
        Speak("Download completed")
    elif dType == 'music':
        results = YoutubeSearch(search, max_results=1).to_dict()
        url = "https://www.youtube.com" + str(results[0]["url_suffix"])
        video = new(url)

        stream = video.getbestaudio()

        # getting filename of stream
        fileName = str(stream.filename)
        if path.exists('Downloaded Music') == False:
            os.mkdir("Downloaded Music")
            speakPrint(
                '"Downloaded Music" folder has successfully been created')
        Speak("Downloading")
        stream.download()
        shutil.move(fileName, f"Downloaded Music/{fileName}")
        Speak("Download completed")
