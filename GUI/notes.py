from GUI.app import THEME
import json
import os
from tkinter import *
import functools


# class Note():
#     def __init__(self, note_text, date):
#         self.note_text = note_text
#         self.date = date

#     def __str__(self):
#         return f"[Note]: {self.note_text}\n[Date]: {self.date}"

#     def get_text(self):
#         return self.note_text

#     def get_date(self):
#         return self.date

class ScrollableFrame(Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = Canvas(self, background=THEME['Background'])
        scrollbar = Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = Frame(canvas, background=THEME['Background'])

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window(
            (0, 0), window=self.scrollable_frame, width=380, anchor='nw')

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=LEFT)
        scrollbar.pack(side=RIGHT, fill="y")


class Notes_Gui():
    def __init__(self):

        self.path = os.path.join("data", "notes.json")

        self.root = Tk(screenName="Notes")
        self.root.title('Notes - Virtual Assistant')
        self.root.iconbitmap("Icon\icon.ico")
        self.root.geometry("400x300")
        self.root.configure(bg=THEME['Background'])

        self.scrollableFrame = ScrollableFrame(self.root)

        self.root.resizable(False, False)

        self.bottom_frame = Frame(self.root, background=THEME['Background'])

        self.new_button = Button(
            self.bottom_frame, text="Add New", command=self.new_note)

        self.save = Button(
            self.bottom_frame, text="Save", command=self.save_notes)

        self.new_button.pack(side=LEFT, padx=10)
        self.save.pack(side=RIGHT, padx=10)

        self.bottom_frame.pack(side=BOTTOM, padx=10, pady=10)

        self.notes = []

        self.load_notes()

        self.frames = []

        for note in self.notes:
            self.new_frame(note['text'])

        self.update()
        self.scrollableFrame.pack()
        self.root.mainloop()

    def new_note(self, text=""):
        self.notes.append({'text': text})
        self.new_frame(text)

    def new_frame(self, text=""):
        def flip_in_edit(frame):
            frame.in_edit = not frame.in_edit
            self.update()

        def delete_note(frame):
            for i in range(len(self.frames)):
                if frame == self.frames[i]:
                    del self.notes[i]
                    self.frames[i].forget()
                    del self.frames[i]
                    self.update()

        self.frames.append(
            Frame(self.scrollableFrame.scrollable_frame))
        frame = self.frames[-1]
        frame.pack(fill=X)

        frame.in_edit = False
        frame.text = text

        frame.pack(side=BOTTOM, padx=5, pady=5)

        frame.edit_button = Button(
            frame, text="Edit", fg="blue", command=functools.partial(flip_in_edit, frame))

        frame.delete_button = Button(
            frame, text="Delete", fg="red", command=functools.partial(delete_note, frame))

        frame.delete_button.pack(side=RIGHT, padx=10, pady=10)
        frame.edit_button.pack(side=RIGHT, padx=10, pady=10)

        frame.text = Text(frame)
        frame.text.insert(END, text)
        frame.text.config(height=int(
            frame.text.index('end').split('.')[0]) - 1, state=DISABLED)
        self.update()

    def update(self):
        for frame in self.frames:
            frame.edit_button.config(text='Done' if frame.in_edit else "Edit")
            if frame.in_edit:
                frame.text.config(state=NORMAL)
                frame.text.config(height=int(
                    frame.text.index('end').split('.')[0]) - 1)
            else:
                frame.text.config(height=min(
                    int(frame.text.index('end').split('.')[0]) - 1, 2))
                frame.text.config(state=DISABLED)
            frame.text.pack(side=LEFT,  padx=10, pady=10)

    def load_notes(self):
        if os.path.exists(self.path):
            with open(self.path, "r") as f:
                self.notes = self.deserialize(f.read())
        else:
            self.notes = []

    def save_notes(self):
        for i in range(len(self.frames)):
            self.notes[i]['text'] = str(
                self.frames[i].text.get("1.0", END)).strip()

        with open(self.path, "w") as f:
            f.write(self.serialize())

    def serialize(self):
        return json.dumps(self.notes)

    def deserialize(self, serialized_text):
        return json.loads(serialized_text)


x = Notes_Gui()
