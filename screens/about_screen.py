from tkinter import Label, Button
from typing import override

from screens.abstract_screen import AbstractScreen
from utils import Utils


class AboutScreen(AbstractScreen):

    @override
    def title_label_widget(self):
        pass

    @override
    def info_label_widget(self):
        return Label(self, text="Hello World!", font=self.font.app_default())

    @override
    def action_button_widget(self):
        return Button(self, text="Späť", font=self.font.app_default(), command=lambda: Utils.go_back_to_main_screen(self))

    @override
    def populate_screen(self):
        pass