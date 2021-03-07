from youtube_search import YoutubeSearch
from pafy import new
from app import Speak


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
        q = input("Choose quality to download: ")
        Speak("Downloading")
        stream[int(q)].download()
        Speak("Download completed")
    elif dType == 'music':
        results = YoutubeSearch(search, max_results=1).to_dict()
        url = "https://www.youtube.com" + str(results[0]["url_suffix"])
        video = new(url)

        stream = video.getbestaudio()

        Speak("Downloading")
        stream.download()
        Speak("Download completed")
