from youtube_search import YoutubeSearch
from pafy import new
import shutil
import os.path
from os import path


class Download:
    def youtube_search(self, title):
        results = YoutubeSearch(title, max_results=1).to_dict()
        url = "https://www.youtube.com" + str(results[0]["url_suffix"])
        video = new(url)
        self.stream = video.allstreams
        self.bestaudio = video.getbestaudio()

    def youtube_download(self, _in, _out):
        title = _in("Please enter the title of the video: ")
        self.youtube_search(title)

        buffer = ""
        for i in range(len(self.stream)):
            buffer += f"{i}: {self.stream[i]} \n"
        _out(buffer[:-2], True)

        # For first time users
        if path.exists('Downloaded Videos') == False:
            buffer = "Please Note That: \n"
            buffer += "'audio' is audio only without video \n"
            buffer += "'video' is video without audio \n"
            buffer += "'normal' is both"
            _out(buffer)

        quality = _in("Choose the quality to download: ")

        # For first time users
        if path.exists('Downloaded Videos') == False:
            os.mkdir("Downloaded Videos")
            _out('"Downloaded Videos" folder has successfully been created')

        # Starrt downloading
        fileName = str(self.stream[int(quality)].filename)
        _out("Downloading")
        self.stream[int(quality)].download()
        shutil.move(fileName, f"Downloaded Videos/{fileName}")
        _out("Download completed")

    def music_download(self, _in, _out):
        title = _in("Please enter the title of the music: ")
        self.youtube_search(title)

        # For first time users
        if path.exists('Downloaded Music') == False:
            os.mkdir("Downloaded Music")
            _out('"Downloaded Music" folder has successfully been created')

        # Start Downloading
        fileName = str(self.bestaudio.filename)
        _out("Downloading")
        self.bestaudio.download()
        shutil.move(fileName, f"Downloaded Music/{fileName}")
        _out("Download completed")

        # Has no meaning (:
        _out('Remember That You can convert the music to mp3\nJust say "Convert"')
