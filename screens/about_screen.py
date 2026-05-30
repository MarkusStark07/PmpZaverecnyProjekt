from tkinter import Label, Button
from typing import override

from constants import Constants
from screens.abstract_screen import AbstractScreen
from utils import Utils


class AboutScreen(AbstractScreen):

    @override
    def title_label_widget(self):
        return Label(self, text="O programe", font=self.font.custom_size(Constants.defaultFontTitleSize))

    @override
    def info_label_widget(self):
        return Label(self, text="Tento program je proof of concept šifrovanej komunikácie cez rádiové vlny. \n Aplikácia šifruje a dešifruje správy cez xor šifru používateľom zadaným klúčom.", font=self.font.app_default())

    @override
    def action_button_widget(self):
        return Button(self, text="Späť", font=self.font.app_default(), command=lambda: Utils.go_back_to_main_screen(self))

    @override
    def populate_screen(self):
        pass