from tkinter import Frame, Label
from tkinter.ttk import Button

from utils import Utils


class SendScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        title_label = Label(self, text="Send Screen")
        title_label.pack(pady=20)

        info_label = Label(self, text="This is the send screens.")
        info_label.pack(pady=20)

        back_button = Button(self, text="Back", command=lambda: Utils.go_back(self))
        back_button.pack(pady=20)