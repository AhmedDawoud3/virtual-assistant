from youtube_search import YoutubeSearch
from pafy import new
from time import sleep
import vlc
import threading


class Music():
    def __init__(self):
        self.music = None
        self.i = 0

    def search_and_play(self, title):
        results = YoutubeSearch(title, max_results=10).to_dict()
        self.i = 0

        # Stop current music
        if self.music != None:
            self.music.stop()

        # Prepare queue
        self.music_list = []
        search = threading.Thread(target=self.search, args=(results, ))
        search.daemon = True
        search.start()

        # Start playing music
        while True:
            try:
                self.music = self.music_list[self.i]
                self.play()
            except IndexError:
                continue
            break

        # Start next music automatically
        play_after_ending = threading.Thread(target=self.play_next_after_and)
        play_after_ending.daemon = True
        play_after_ending.start()

    # To prepare queue
    def search(self, results):
        for result in results:
            url = "https://www.youtube.com" + str(result["url_suffix"])
            video = new(url)
            self.music_list.append(vlc.MediaPlayer(
                video.allstreams[1].url))

    # A use it to play music to avoid unexpected error
    def play(self):
        while True:
            self.music.play()
            print("Trying start music")
            sleep(1)
            if self.music.is_playing():
                print(f"Music started: {self.music.get_title()}")
                break

    # To start next music automatically
    def play_next_after_and(self):
        while True:
            # if (self.music.get_position() >= 0.99):
            #     print(f"Finishing {self.music.get_position()}")
            # if (round(self.music.get_position(), 3) == 0.999):
            if self.music.get_length() - self.music.get_time() < 1000 and self.music.get_length() != 0:
                print(
                    f"{self.music.get_length()} : {self.music.get_time()} : {self.music.get_position() * 100}%")
                self.next()

    # Pause and Continue
    def pause_continue(self):
        self.music.pause()

    # Play next music
    def next(self):
        self.i += 1
        self.music.stop()
        self.music = self.music_list[self.i]
        self.play()
        print("Playing next music")

    # Play Previous
    def prev(self):
        self.i -= 1
        self.music.stop()
        self.music = self.music_list[self.i]
        self.play()

    def is_playing(self):
        if self.music != None:
            return self.music.is_playing()

    # Stop music for safe exit
    def stop(self):
        if self.music != None:
            self.music.stop()
