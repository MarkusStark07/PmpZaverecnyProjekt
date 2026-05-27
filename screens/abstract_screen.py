from abc import ABC, abstractmethod
from tkinter import Frame


# Abstraktná trieda z ktorej vychádzajú všetky obrazovky
# Opisuje základnú štruktúru obrazovky
class AbstractScreen(Frame, ABC):
    def __init__(self, parent, controller, font_object):
        super().__init__(parent)

        self.controller = controller
        self.font = font_object

        title_label = self.title_label_widget()
        if title_label is not None:
            title_label.place(relx=0.5, rely=0.1, anchor="center")

        info_label = self.info_label_widget()
        if info_label is not None:
            info_label.place(relx=0.5, rely=0.3, anchor="center")

        action_button = self.action_button_widget()
        if action_button is not None:
            action_button.place(relx=0.5, rely=0.9, anchor="center")

        self.populate_screen()

    @abstractmethod
    def title_label_widget(self):
        pass

    @abstractmethod
    def info_label_widget(self):
        pass

    @abstractmethod
    def action_button_widget(self):
        pass

    @abstractmethod
    def populate_screen(self):
        pass
