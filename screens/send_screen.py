from tkinter import Label, Button, Text
from typing import override

from constants import Constants
from screens.abstract_screen import AbstractScreen
from services.message_service import MessageService
from utils import Utils


class SendScreen(AbstractScreen):

    @override
    def title_label_widget(self):
        return Label(self, text="Send Screen", font=self.font.custom_size(Constants.defaultFontTitleSize))

    @override
    def info_label_widget(self):
        return Label(self, text="This is the send screens.", font=self.font.app_default())

    @override
    def action_button_widget(self):
        return Button(self, text="Späť", font=self.font.app_default(), command=lambda: Utils.go_back(self))

    @override
    def populate_screen(self):
        message_input_text_field = Text(self, font=self.font.app_default(), width=20, height=5)
        message_input_text_field.place(relx=0.5, rely=0.5, anchor="center")

        send_message_button = Button(self, text="Odoslať", font=self.font.app_default(), command=lambda: MessageService.send(message_input_text_field.get("1.0", "end-1c")))
        send_message_button.place(relx=0.5, rely=0.7, anchor="center")