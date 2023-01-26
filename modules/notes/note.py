import time


class Note:
    def __init__(self, note=None):
        if note == None:
            self.title = ""
            self.date = int(time.time())
            self.text = ""
        else:
            self.title = note["title"]
            self.date = note["date"]
            self.text = note["text"]

    def get_title(self):
        return self.title

    def get_date(self):
        return self.date

    def get_text(self):
        return self.text

    def get_note(self):
        return {"title": self.get_title(), "date": self.get_date(), "text": self.get_text()}

    def set_title(self, title):
        self.title = title

    def set_date(self):
        self.time = int(time.time())

    def set_text(self, text):
        self.text = text
