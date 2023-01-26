from tkinter import *
from tkfontawesome import icon_to_image
from funcs import THEMES


class GUI:
    def __init__(self, i, get_theme, set_theme):
        self.is_ready = False
        self.THEME = THEMES[i]
        self.get_theme = get_theme
        self.set_theme = set_theme

    def init(self):
        # Initiate GUI Window
        self.root = Tk(screenName="Virtual Assistant")
        self.root.title('Virtual Assistant')
        self.root.iconbitmap("Icon\icon.ico")
        self.root.geometry("400x600")
        self.root.configure(bg=self.THEME['bg'])
        self.root.resizable(False, False)

        # Fontawesome icons
        self.theme_icon = [
            icon_to_image(
                "adjust", fill=THEMES[0]["user"], scale_to_width=10),
            icon_to_image(
                "adjust", fill=THEMES[1]["user"], scale_to_width=10)
        ]

        # To control up and down keys
        self.queue = []
        self.queue_i = 0

        # To  control messages appearence
        self.messages = []

        self.load_theme()
        self.is_ready = True

        self.root.mainloop()

    def load_theme(self):
        # The main frame to easily change theme
        self.main_frame = Frame(self.root, background=self.THEME["bg"])
        self.main_frame.pack(fill="both", expand=True)

        # Set current Theme
        current_theme = self.get_theme()
        new_theme = 1 if current_theme == 0 else 0

        # Change theme button
        theme_btn = Button(self.main_frame, image=self.theme_icon[new_theme],
                           background=self.THEME["app"], command=lambda: self.gui_change_theme(new_theme), activebackground=self.THEME["app"], width=20, height=20)
        theme_btn.place(in_=self.main_frame, relx=0.95,
                        rely=0.03, anchor=CENTER)

        # Make and place entry field
        in_frame = Frame(
            self.main_frame, background=self.THEME['bg'], padx=10, pady=10)
        in_frame.pack(side=BOTTOM)

        Frame(self.main_frame, background=self.THEME["text"],
              borderwidth=2, width=400).pack(side=BOTTOM)

        self.e = Entry(in_frame, background=self.THEME['app'], foreground=self.THEME["text"], width=60,
                       borderwidth=2)

        self.e.pack(side=BOTTOM, anchor="w", padx=10, pady=10)
        self.e.focus_set()

    # Show th app output
    def gui_out(self, text):
        self.display_message(
            text, "left", self.THEME["app"], self.THEME["text"], 0)

    # Show the user input
    def gui_in(self, text):
        self.queue.append(text)
        self.queue_i = len(self.queue)
        self.display_message(
            text, "right", self.THEME["user"], self.THEME["bg"], 1)

    def display_message(self, text, justify, background, foreground, arg3):
        label = Label(
            self.main_frame,
            text=text,
            justify=justify,
            background=background,
            padx=5,
            pady=5,
            foreground=foreground
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
        return self.root.focus_displayof()

    def entry_up(self):
        if self.queue_i != 0 and self.is_focused():
            self.queue_i -= 1
            self.clear_entry()
            self.e.insert(0, self.queue[self.queue_i])

    def entry_down(self):
        if self.is_focused():
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
            if self.messages[i-x-1][0] == 0:
                self.messages[i-x-1][1].pack(side=BOTTOM,
                                             anchor="w", padx=5, pady=5)

            # User input
            else:
                self.messages[i-x-1][1].pack(side=BOTTOM,
                                             anchor="e", padx=5, pady=5)

    def gui_change_theme(self, i):
        self.THEME = THEMES[i]
        self.main_frame.forget()
        print(f"Setting Theme {i}")
        self.set_theme(i)
        self.load_theme()

    # Destroy the window for safe exit
    def gui_destroy(self):
        self.root.destroy()
