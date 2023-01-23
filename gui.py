from tkinter import *
import threading
from time import sleep
import keyboard


class GUI:
    def __init__(self):
        self.is_ready = False

    def init(self):
        # Initiate GUI Window
        self.root = Tk(screenName="Virtual Assistant")
        self.root.geometry("400x600")
        self.root.configure(bg="#CEE5D0")
        self.root.resizable(False, False)

        # Make and place entry field
        in_frame = Frame(background="#ddd", padx=10, pady=10)
        in_frame.pack(side=BOTTOM)
        self.e = Entry(in_frame, background="#eee", width=60,
                       borderwidth=2)
        self.e.pack(side=BOTTOM, anchor="w", padx=10, pady=10)

        # To  control messages appearence
        self.queue = []

        self.is_ready = True
        self.root.mainloop()

    # Show th app output
    def gui_out(self, text):
        label = Label(self.root, text=text, justify="left",
                      background="#F3F0D7", padx=5, pady=5, fg="#000")
        label.bind('<Configure>', lambda e: label.config(
            wraplength=label.winfo_width()))
        self.queue.append((0, label))
        self.gui_render()

    # Show the user input
    def gui_in(self, text):
        label = Label(self.root, text=text, justify="right",
                      background="#E0C097", padx=5, pady=5, fg="#000")
        label.bind('<Configure>', lambda e: label.config(
            wraplength=label.winfo_width()))
        self.queue.append((1, label))
        self.gui_render()

    # Get entry text from the user
    def gui_get_text(self):
        return self.e.get()

    # Clear entry text
    def clear_entry(self):
        self.e.delete(0, END)

    # Render the messages on the screen when new message is snet
    def gui_render(self):
        i = len(self.queue)
        for x in range(i):
            self.queue[x][1].forget()
        for x in range(i):
            # App output
            if self.queue[i-x-1][0] == 0:
                self.queue[i-x-1][1].pack(side=BOTTOM,
                                          anchor="w", padx=5, pady=5)

            # User input
            else:
                self.queue[i-x-1][1].pack(side=BOTTOM,
                                          anchor="e", padx=5, pady=5)

    # Destroy the window for safe exit
    def gui_destroy(self):
        self.root.destroy()
