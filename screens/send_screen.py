from tkinter import Label, Button
from typing import override

from constants import Constants
from screens.abstract_screen import AbstractScreen
from utils import Utils


class SendScreen(AbstractScreen):
    @override
    def populate_screen(self):
        title_label = Label(self, text="Send Screen", font=self.font.custom_size(Constants.defaultFontTitleSize))
        title_label.place(relx=0.5, rely=0.1, anchor="center")

        info_label = Label(self, text="This is the send screens.", font=self.font.app_default())
        info_label.place(relx=0.5, rely=0.3, anchor="center")

        back_button = Button(self, text="Back", font=self.font.app_default(), command=lambda: Utils.go_back(self))
        back_button.place(relx=0.5, rely=0.9, anchor="center")