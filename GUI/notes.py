from funcs import THEMES
from tkinter import *
import tkinter.font as font
import time
from functools import partial
from tkfontawesome import icon_to_image
from GUI.scrollableframe import ScrollableFrame
import keyboard

THEME = THEMES[0]


class Notes_GUI:
    def __init__(self, notes_obj):
        self.THEME = THEME
        self.root = Tk(screenName="Notes")
        self.root.title("Notes - Virtual Assistant")
        self.root.iconbitmap("Icon\icon.ico")
        self.root.geometry("400x600")
        self.root.configure(bg=self.THEME["bg"])
        self.root.resizable(False, False)

        # Main frame that contains notes and Add notes button
        self.main_frame = Frame(self.root, background=self.THEME["bg"])
        self.main_frame.pack(fill="both", expand=True)

        # Scrollable bar that contains notes
        self.main_data = ScrollableFrame(
            self.main_frame, background=self.THEME["bg"])
        self.main_data.pack(fill="both", expand=True)
        # self.main_data.pack()

        # Fontawesome icons
        self.save_icon = icon_to_image(
            "check", fill=self.THEME["user"], scale_to_width=20)
        self.plus_icon = icon_to_image(
            "plus-circle", fill=self.THEME["user"], scale_to_width=30)

        # Add note button
        self.add = Button(self.main_frame, image=self.plus_icon,
                          background=self.THEME["app"], command=self.add_note, activebackground=self.THEME["app"], width=40, height=40)

        self.add.place(in_=self.main_frame, relx=0.9, rely=0.93, anchor=CENTER)

        # Load Saved notes
        self.notes_obj = notes_obj
        self.note_list = notes_obj.note_list

        self.load()
        self.root.mainloop()

    # Read Notes and Show GUI
    def load(self):
        self.notes_frames = []
        for note in self.note_list:
            # Set A frame for the note
            note_frame = Frame(
                self.main_data.scrollable_frame, background=self.THEME["app"], padx=5, pady=5, highlightthickness=2, highlightbackground=self.THEME["user"])
            note_frame.pack(padx=10, pady=10, fill='both')
            self.notes_frames.append(note_frame)

            data_frame = Frame(note_frame, background=self.THEME["app"])
            data_frame.grid()

            # Show note title
            title = note.get_title()
            title_label = Label(data_frame, text=title,
                                background=self.THEME["app"], foreground=self.THEME["text"])
            title_label["font"] = font.Font(size=12)
            title_label.grid(column=0, row=0, sticky="w")

            # Show note date
            date = time.strftime("%m/%d", time.gmtime(note.get_date()))

            date_label = Label(data_frame, text=date,
                               background=self.THEME["app"], foreground=self.THEME["text"])
            date_label.grid(column=1, row=0, sticky="e")

            # Show note text
            text = note.get_text()
            text_label = Label(data_frame, text=text,
                               justify=LEFT, anchor="w", background=self.THEME["app"], foreground=self.THEME["text"], width=47)
            text_label.grid(column=0, row=1, columnspan=2, sticky="w")

            # Delete note icon
            delete_btn = Button(note_frame, text="X",
                                background=self.THEME["app"], padx=5, borderwidth=1, activebackground=self.THEME["app"], foreground=self.THEME["text"], command=partial(self.delete_note_alert, note))
            delete_btn.grid(column=2, row=0, rowspan=2, sticky="e", padx=5)

            data_frame.bind("<Button-1>", partial(self.edit_note, note))
            title_label.bind("<Button-1>", partial(self.edit_note, note))
            date_label.bind("<Button-1>", partial(self.edit_note, note))
            text_label.bind("<Button-1>", partial(self.edit_note, note))

        # Load Notes GUI
        self.main_frame.pack(fill="both", expand=True)
        # self.main_data.pack()

        keyboard.add_hotkey("esc", self.quit)

    def add_note(self):
        note = self.notes_obj.add_note()
        self.edit_note(note)

    def edit_note(self, note, event=None):
        # Forget main frame
        self.main_frame.forget()
        keyboard.remove_hotkey("esc")

        # Initiate a frame to edit the note
        self.edit_note_frame = Frame(
            self.root, background=self.THEME["app"], highlightthickness=2, highlightbackground=self.THEME["user"], highlightcolor=self.THEME["user"])
        self.edit_note_frame.pack(fill="both", padx=10, pady=10)

        # An Entry for note title
        self.current_note_title = Entry(self.edit_note_frame,
                                        background=self.THEME["app"], foreground=self.THEME["text"], width=60, borderwidth=0)
        self.current_note_title.insert(0, note.get_title())
        self.current_note_title["font"] = font.Font(size=12)
        self.current_note_title.pack(padx=10, pady=10)

        # A Horizontal separator between title and text
        Frame(self.edit_note_frame, background=self.THEME["text"],
              borderwidth=2, width=400).pack()

        # A Text field for note text
        self.current_note_text = Text(self.edit_note_frame, background=self.THEME["app"], foreground=self.THEME["text"],
                                      width=60, height=32, borderwidth=0)
        self.current_note_text.insert("1.0", note.get_text())
        self.current_note_text.pack(padx=10, pady=10)

        # Save note button
        save = Button(self.edit_note_frame, image=self.save_icon,
                      background=self.THEME["app"], command=lambda: self.save_note(note), activebackground=self.THEME["app"], width=40, height=40)

        save.place(in_=self.edit_note_frame,
                   relx=0.925, rely=0.955, anchor=CENTER)

        # Esc from keyboard
        keyboard.add_hotkey("esc", self.save_note, (note, ))

    def save_note(self, note):
        # To Make sure that window is focused to avoid unexpected results due to keyboard "esc" hotkey
        if not self.root.focus_displayof():
            return

        # To avoid "note" argument confliction
        keyboard.remove_hotkey("esc")

        # Get data to compare
        old_title = note.get_title()
        new_title = self.current_note_title.get()

        old_text = note.get_text()
        new_text = self.current_note_text.get("1.0",  'end-1c')

        # Two Entries are empty
        if new_title == "" and new_text == "":
            self.notes_obj.delete_note(note)

        # Title or Text has changed
        elif new_title != old_title or new_text != old_text:
            note.set_title(new_title)
            note.set_date()
            note.set_text(new_text)

        # Back to main frame
        self.edit_note_frame.forget()
        self.reload()

    # Show Delete note alert
    def delete_note_alert(self, note):
        # Forget main frame
        self.main_frame.forget()
        keyboard.remove_hotkey("esc")

        # Load alert main frame
        self.alert_frame = Frame(self.root, background=self.THEME["bg"])
        self.alert_frame.pack(fill="both", expand=True)

        # Alert container frame
        box_frame = Frame(
            background=self.THEME["app"], padx=20, pady=20, highlightthickness=2, highlightbackground=self.THEME["user"])
        box_frame.place(in_=self.alert_frame, anchor="c", relx=.5, rely=.4)

        # Show Alert Text
        Label(box_frame, text="Are you sure you want to delete?", padx=5, pady=5,
              background=self.THEME["app"], foreground=self.THEME["text"]).pack()

        # An Empty Label to adjust alert box design
        Label(box_frame, pady=10, background=self.THEME["app"]).pack()

        # Respond Buttons
        accept_btn = Button(box_frame, text="Yes", padx=10, pady=5,
                            background=self.THEME["user"], activebackground=self.THEME["user"], foreground=self.THEME["bg"], command=lambda: self.delete_note_alert_reponse(True, note))
        accept_btn.pack(side=LEFT, padx=20)

        refuse_btn = Button(box_frame, text="No", padx=10, pady=5,
                            background=self.THEME["app"], activebackground=self.THEME["app"], foreground=self.THEME["text"], command=lambda: self.delete_note_alert_reponse(False, note))
        refuse_btn.pack(side=RIGHT, padx=20)

        # Enter for "Yes", Esc for "No"
        keyboard.add_hotkey(
            "enter", self.delete_note_alert_reponse, (True, note, ))

        keyboard.add_hotkey(
            "esc", self.delete_note_alert_reponse, (False, note, ))

    # User responded to Delete note alert
    def delete_note_alert_reponse(self, reponse, note):
        # To Make sure that window is focused to avoid unexpected results due to keyboard "esc" hotkey
        if not self.root.focus_displayof():
            return

        # To avoid "note" argument confliction
        keyboard.remove_hotkey("enter")
        keyboard.remove_hotkey("esc")

        # If Delete Confirmed
        if reponse:
            self.notes_obj.delete_note(note)

        # Back to Main frame
        self.alert_frame.forget()
        self.reload()

    # Save data and reload main frame
    def reload(self):
        self.notes_obj.note_list = sorted(
            self.note_list, key=lambda d: d.get_date(), reverse=True)
        self.note_list = self.notes_obj.note_list
        self.notes_obj.save()
        for frame in self.notes_frames:
            frame.destroy()
        self.load()

    # Quit from esc key
    def quit(self):
        if not self.root.focus_displayof():
            return

        self.root.destroy()
