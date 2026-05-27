from tkinter import Label, Button
from typing import override

from constants import Constants
from screens.about_screen import AboutScreen
from screens.abstract_screen import AbstractScreen
from screens.listen_screen import ListenScreen
from utils import Utils


class MainScreen(AbstractScreen):
    @override
    def populate_screen(self):
        title_label = Label(self, text="Hlavné Menu", font=self.font.custom_size(Constants.defaultFontTitleSize))
        title_label.place(relx=0.5, rely=0.1, anchor="center")

        info_label = Label(self, text="Vyberte akciu", font=self.font.app_default())
        info_label.place(relx=0.5, rely=0.3, anchor="center")

        listen_screen_button = Button(self, text="Počúvať", font=self.font.app_default(), command=lambda: Utils.show_screen(self.controller, ListenScreen, self.font))
        listen_screen_button.place(relx=0.4, rely=0.5, anchor="center")

        send_screen_button = Button(self, text="Odoslať", font=self.font.app_default(), command=lambda: Utils.show_screen(self.controller, ListenScreen, self.font))
        send_screen_button.place(relx=0.6, rely=0.5, anchor="center")

        about_screen_button = Button(self, text="About", font=self.font.app_default(), command=lambda: Utils.show_screen(self.controller, AboutScreen, self.font))
        about_screen_button.place(relx=0.5, rely=0.9, anchor="center")