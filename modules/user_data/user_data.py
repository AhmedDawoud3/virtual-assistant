import json
import os


class UserData:
    def __init__(self):
        self.path = os.path.join("data", "user.json")
        with open(self.path, "r") as f:
            self.data = json.loads(f.read())

    def update_data_file(self):
        with open(self.path, "w") as f:
            f.write(json.dumps(self.data))

    def get_name(self):
        return self.data['username']

    def get_city(self):
        return self.data['city']

    def get_voice(self):
        return self.data['voice']

    def set_name(self, name):
        self.data['username'] = name
        self.update_data_file()

    def set_city(self, city):
        self.data['city'] = city
        self.update_data_file()

    def set_voice(self, voice):
        self.data['voice'] = voice
        self.update_data_file()
