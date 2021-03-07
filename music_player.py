from youtube_search import YoutubeSearch
from pafy import new
import vlc


def music_player(search, music):
    results = YoutubeSearch(search, max_results=10).to_dict()

    if music != None:
        music.stop()

    music_list = []

    for result in results:

        url = "https://www.youtube.com" + str(result["url_suffix"])

        video = new(url)

        music_list.append(vlc.MediaPlayer(video.allstreams[1].url))

    media = music_list[0]
    media.play()

    return media, music_list


def pause_music(music):
    music.pause()


def next_music(music, music_list):
    for i in range(len(music_list)):
        if music_list[i] == music:
            music.stop()
            music_list[i + 1].play()
            return music_list[i + 1]
