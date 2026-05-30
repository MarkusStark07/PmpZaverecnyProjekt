from tkinter import Label, Button, Text
from typing import override

from constants import Constants
from domain.config import Config
from screens.abstract_screen import AbstractScreen
from services.storage.config_storage_service import ConfigStorageService
from utils import Utils


class ConfigScreen(AbstractScreen):

    def __init__(self, parent, controller, font_object):
        self.serial_port_input_text_field = None
        self.key_input_text_field = None
        self.serial_speed_input_text_field = None
        super().__init__(parent, controller, font_object)

    @override
    def title_label_widget(self):
        return Label(self, text="Obrazovka Nastavení", font=self.font.custom_size(Constants.defaultFontTitleSize))

    @override
    def info_label_widget(self):
        pass

    @override
    def action_button_widget(self):
        return Button(self, text="Uložiť", font=self.font.app_default(), command=lambda: self.save_config())

    @override
    def populate_screen(self):
        key_input_info_label = Label(self, text="Nastavenia šifrovacieho klúča", font=self.font.app_default())
        key_input_info_label.place(relx=0.5, rely=0.2, anchor="center")

        self.key_input_text_field = Text(self, font=self.font.app_default(), width=20, height=2)
        saved_encryption_key = ConfigStorageService().get(Config.ENCRYPTION_KEY)
        self.key_input_text_field.insert("1.0", saved_encryption_key)
        self.key_input_text_field.place(relx=0.5, rely=0.3, anchor="center")

        serial_speed_info_label = Label(self, text="Nastavenia serial rýchlosti prenosu", font=self.font.app_default())
        serial_speed_info_label.place(relx=0.5, rely=0.4, anchor="center")

        self.serial_speed_input_text_field = Text(self, font=self.font.app_default(), width=20, height=2)
        saved_serial_speed = ConfigStorageService().get(Config.SERIAL_SPEED)
        self.serial_speed_input_text_field.insert("1.0", saved_serial_speed)
        self.serial_speed_input_text_field.place(relx=0.5, rely=0.5, anchor="center")

        serial_port_info_label = Label(self, text="Nastavenia serial portu", font=self.font.app_default())
        serial_port_info_label.place(relx=0.5, rely=0.6, anchor="center")

        self.serial_port_input_text_field = Text(self, font=self.font.app_default(), width=20, height=2)
        saved_serial_port = ConfigStorageService().get(Config.SERIAL_PORT)
        self.serial_port_input_text_field.insert("1.0", saved_serial_port)
        self.serial_port_input_text_field.place(relx=0.5, rely=0.7, anchor="center")


    def save_config(self):
        # Uloženie zadaných hodnôt do úložiska
        encryption_key = self.key_input_text_field.get("1.0", "end-1c")
        ConfigStorageService().save(Config.ENCRYPTION_KEY, encryption_key)

        serial_speed = self.serial_speed_input_text_field.get("1.0", "end-1c")
        ConfigStorageService().save(Config.SERIAL_SPEED, serial_speed)

        serial_port = self.serial_port_input_text_field.get("1.0", "end-1c")
        ConfigStorageService().save(Config.SERIAL_PORT, serial_port)

        Utils.go_back_to_main_screen(self)