from tkinter import Label, Button
from typing import override

from constants import Constants
from screens.abstract_screen import AbstractScreen
from services.message_service import MessageService
from utils import Utils


class ListenScreen(AbstractScreen):
    def __init__(self, parent, controller, font_object):
        self.received_text_label = None
        super().__init__(parent, controller, font_object)

    @override
    def title_label_widget(self):
        return Label(self, text="Listen Screen", font=self.font.custom_size(Constants.defaultFontTitleSize))

    @override
    def info_label_widget(self):
        return Label(self, text="This is the listen screens.", font=self.font.app_default())

    @override
    def action_button_widget(self):
        return Button(self, text="Späť", font=self.font.app_default(), command=lambda: Utils.go_back_to_main_screen(self))

    @override
    def populate_screen(self):
        self.received_text_label = Label(self, text="Počúvam...", font=self.font.app_default())
        self.received_text_label.place(relx=0.5, rely=0.5, anchor="center")

        # Zobrazenie príjmutej správy
        received_message = MessageService().receive()
        self.received_text_label.config(text=received_message)