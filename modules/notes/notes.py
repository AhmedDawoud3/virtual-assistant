from modules.notes.note import Note
import json
import os


class Notes:
    def __init__(self):
        self.path = os.path.join("data", "notes.json")
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                data = json.loads(file.read())

        self.note_list = []
        for note in data:
            self.note_list.append(Note(note))

    def add_note(self):
        note = Note()
        self.note_list.append(note)
        return note

    def delete_note(self, note):
        self.note_list.remove(note)

    # Save after delete or edit
    def save(self):
        with open(self.path, "w") as file:
            file.write(json.dumps(self.get_notes()))

    # Get text to json dump
    def get_notes(self):
        data = []
        for note in self.note_list:
            data.append(note.get_note())
        return data
