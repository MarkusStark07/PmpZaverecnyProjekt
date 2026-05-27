from tkinter import Label, Button
from typing import override

from constants import Constants
from screens.abstract_screen import AbstractScreen
from utils import Utils


class ListenScreen(AbstractScreen):

    @override
    def title_label_widget(self):
        return Label(self, text="Listen Screen", font=self.font.custom_size(Constants.defaultFontTitleSize))

    @override
    def info_label_widget(self):
        return Label(self, text="This is the listen screens.", font=self.font.app_default())

    @override
    def action_button_widget(self):
        return Button(self, text="Back", font=self.font.app_default(), command=lambda: Utils.go_back(self))

    @override
    def populate_screen(self):
        pass