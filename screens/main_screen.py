from tkinter import Frame, Label, Button

from screens.listen_screen import ListenScreen
from utils import Utils


class MainScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        title_label = Label(self, text="Main Screen")
        title_label.pack(pady=20)

        info_label = Label(self, text="This is the main screens.")
        info_label.pack(pady=20)

        listen_screen_button = Button(self, text="Listen Screen", command=lambda: Utils.show_screen(self.controller, ListenScreen))
        listen_screen_button.pack(pady=20)

        send_screen_button = Button(self, text="Send Screen", command=lambda: Utils.show_screen(self.controller, ListenScreen))
        send_screen_button.pack(pady=20)