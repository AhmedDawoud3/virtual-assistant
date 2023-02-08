from modules.notes.note import Note
import json
import os


class Notes:
    def __init__(self):
        self.path = os.path.join("data", "notes.json")
        if os.path.exists(self.path):
            with open(self.path, "r") as file:
                data = json.loads(file.read())
        else:
            data = []
            
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

    # ---------------------------------------------
    # ------------- Virtual Assistant -------------
    # ---------------------------------------------
    def va_show_notes(self, _in, _out):
        _out("Ok. Your notes are: ", write=False)
        for i in range(len(self.note_list)):
            note = self.note_list[i]
            _out(f"{i + 1}: {note.get_title()} \n{note.get_text()}")

    def va_delete_note(self, _in, _out):
        try:
            num = int(_in("Enter the number of the note delete: "))
            note = self.note_list[num - 1]
        except:
            _out("Sorry, No note with this number")
            return
        self.delete_note(note)
        self.save()
        _out("Note has successfully been deleted")

    def va_add_note(self, _in, _out):
        self.va_edit_note(_in, _out, new=True)

    def va_edit_note(self, _in, _out, new=False):
        # Add new note
        if new:
            note = self.add_note()
        else:
            num = int(_in("Enter the number of the note to edit: "))
            try:
                note = self.note_list[num - 1]
            except IndexError:
                note = self.add_note()
                _out("Sorry the number is wrong")
                _out("you are about to add new note", write=False)

        # Get old data
        old_title = note.get_title()
        old_text = note.get_text()

        # Get new title
        _out("Enter the title: ")
        _out("Leave empty to keep the value unchanged", write=False)
        new_title = _in("")

        # Get new text
        _out("Enter the text: ")
        _out("Leave empty to keep the value unchanged", write=False)
        new_text = _in("")

        # Title or Text has changed
        if new_title != old_title or new_text != old_text:
            note.set_title(new_title)
            note.set_date()
            note.set_text(new_text)

        self.note_list = sorted(
            self.note_list, key=lambda d: d.get_date(), reverse=True)

        self.save()
        _out("Ok. Your note has successfully been saved")
        print("Saving")
