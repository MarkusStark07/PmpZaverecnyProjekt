from tkinter import Label, Button
from typing import override

from constants import Constants
from screens.abstract_screen import AbstractScreen
from utils import Utils


class SendScreen(AbstractScreen):
    def title_label_widget(self):
        return Label(self, text="Send Screen", font=self.font.custom_size(Constants.defaultFontTitleSize))

    def info_label_widget(self):
        return Label(self, text="This is the send screens.", font=self.font.app_default())

    def action_button_widget(self):
        return Button(self, text="Back", font=self.font.app_default(), command=lambda: Utils.go_back(self))

    @override
    def populate_screen(self):
        pass