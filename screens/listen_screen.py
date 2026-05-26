from tkinter import Frame, Label, Button

from utils import Utils


class ListenScreen(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.controller = controller

        title_label = Label(self, text="Listen Screen")
        title_label.pack(pady=20)

        info_label = Label(self, text="This is the listen screens.")
        info_label.pack(pady=20)

        back_button = Button(self, text="Back", command=lambda: Utils.go_back(self))
        back_button.pack(pady=20)