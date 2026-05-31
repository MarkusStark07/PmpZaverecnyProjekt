from tkinter import Label, Button
from typing import override

from app.constants import Constants
from app.screens.about_screen import AboutScreen
from app.screens.abstract_screen import AbstractScreen
from app.screens.config_screen import ConfigScreen
from app.screens.listen_screen import ListenScreen
from app.screens.send_screen import SendScreen
from app.utils import Utils


class MainScreen(AbstractScreen):

    @override
    def title_label_widget(self):
        return Label(self, text="Hlavné Menu", font=self.font.custom_size(Constants.defaultFontTitleSize))

    @override
    def info_label_widget(self):
        return Label(self, text="Vyberte akciu", font=self.font.app_default())

    @override
    def action_button_widget(self):
        return Button(self, text="O programe", font=self.font.app_default(), command=lambda: Utils.show_screen(self.controller, AboutScreen, self.font))

    @override
    def populate_screen(self):

        listen_screen_button = Button(self, text="Počúvať", font=self.font.app_default(), command=lambda: Utils.show_screen(self.controller, ListenScreen, self.font))
        listen_screen_button.place(relx=0.4, rely=0.5, anchor="center")

        send_screen_button = Button(self, text="Odoslať", font=self.font.app_default(), command=lambda: Utils.show_screen(self.controller, SendScreen, self.font))
        send_screen_button.place(relx=0.6, rely=0.5, anchor="center")

        config_screen_button = Button(self, text="Nastavenia", font=self.font.app_default(), command=lambda: Utils.show_screen(self.controller, ConfigScreen, self.font))
        config_screen_button.place(relx=0.5, rely=0.6, anchor="center")