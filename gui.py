from tkinter import *


class GUI:
    def __init__(self):
        self.is_ready = False

    def init(self):
        # Initiate GUI Window
        self.root = Tk(screenName="Virtual Assistant")
        self.root.title('Virtual Assistant')
        self.root.iconbitmap("Icon\icon.ico")
        self.root.geometry("400x600")
        self.root.configure(bg="#CEE5D0")
        # self.root.configure(bg="#eee")
        self.root.resizable(False, False)

        # Make and place entry field
        # in_frame = Frame(background="#B6EADA", padx=10, pady=10)
        # in_frame.pack(side=BOTTOM)

        # self.e = Entry(in_frame, background="#CBEDD5", width=60,
        #                borderwidth=2)

        in_frame = Frame(background="#CEE5D0", padx=10, pady=10)
        in_frame.pack(side=BOTTOM)

        Frame(self.root, background="#ccc", width=600).pack(side=BOTTOM)

        self.e = Entry(in_frame, background="#F3F0D7", width=60,
                       borderwidth=1)
        self.e.pack(side=BOTTOM, anchor="w", padx=10, pady=10)
        self.e.focus_set()

        # To control up and down keys
        self.queue = []
        self.queue_i = 0

        # To  control messages appearence
        self.messages = []

        self.is_ready = True
        self.root.mainloop()

    # Show th app output
    def gui_out(self, text):
        self.display(text, "left", "#F3F0D7", 0)
        # self.display(text, "left", "#e3e0c7", 0)

        # Show the user input
    def gui_in(self, text):
        self.queue.append(text)
        self.queue_i = len(self.queue)
        self.display(text, "right", "#E0C097", 1)
        # self.display(text, "right", "#f9e4cb", 1)

    def display(self, text, justify, background, arg3):
        label = Label(
            self.root,
            text=text,
            justify=justify,
            background=background,
            padx=5,
            pady=5,
            fg="#000",
        )
        label.bind(
            '<Configure>', lambda e: label.config(
                wraplength=label.winfo_width())
        )
        self.messages.append((arg3, label))
        self.gui_render()

    # Get entry text from the user
    def gui_get_text(self):
        return self.e.get()

    # Clear entry text
    def clear_entry(self):
        self.e.delete(0, END)

    # To Chack if Entry field is focused
    def is_focused(self):
        if self.root.focus_get() == self.e:
            return True

    def entry_up(self):
        if self.queue_i != 0:
            self.queue_i -= 1
            self.clear_entry()
            self.e.insert(0, self.queue[self.queue_i])

    def entry_down(self):
        if self.queue_i < (len(self.queue) - 1):
            self.queue_i += 1
            self.clear_entry()
            self.e.insert(0, self.queue[self.queue_i])
        elif self.queue_i == (len(self.queue) - 1):
            self.queue_i += 1
            self.clear_entry()

    # Render the messages on the screen when new message is snet
    def gui_render(self):
        i = len(self.messages)
        for x in range(i):
            self.messages[x][1].forget()
        for x in range(i):
            # App output
            if self.messages[i-x-1][0] == 0:
                self.messages[i-x-1][1].pack(side=BOTTOM,
                                             anchor="w", padx=5, pady=5)

            # User input
            else:
                self.messages[i-x-1][1].pack(side=BOTTOM,
                                             anchor="e", padx=5, pady=5)

    # Destroy the window for safe exit
    def gui_destroy(self):
        self.root.destroy()
