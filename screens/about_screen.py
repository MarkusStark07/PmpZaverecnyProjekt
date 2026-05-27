from tkinter import Label, Button

from screens.abstract_screen import AbstractScreen
from utils import Utils


class AboutScreen(AbstractScreen):
    def populate_screen(self):
        info_label = Label(self, text="Hello World!", font=self.font.app_default())
        info_label.place(relx=0.5, rely=0.5, anchor="center")

        back_button = Button(self, text="Back", font=self.font.app_default(), command=lambda: Utils.go_back(self))
        back_button.place(relx=0.5, rely=0.9, anchor="center")