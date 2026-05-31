from tkinter import Label, Button
from typing import override

from app.constants import Constants
from app.screens.abstract_screen import AbstractScreen
from app.utils import Utils


class AboutScreen(AbstractScreen):

    @override
    def title_label_widget(self):
        return Label(self, text="O programe", font=self.font.custom_size(Constants.defaultFontTitleSize))

    @override
    def info_label_widget(self):
        return Label(self, text="Tento program je proof of concept desktopovej aplikácie na šifrovanú komunikáciu cez rádiové vlny pomocou microbit mikro-kontrolera. \n Aplikácia šifruje a dešifruje správy cez xor šifru používateľom zadaným klúčom.", font=self.font.app_default())

    @override
    def action_button_widget(self):
        return Button(self, text="Späť", font=self.font.app_default(), command=lambda: Utils.go_back_to_main_screen(self))

    @override
    def populate_screen(self):
        pass