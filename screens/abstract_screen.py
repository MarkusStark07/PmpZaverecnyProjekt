from abc import ABC, abstractmethod
from tkinter import Frame


# Abstraktná trieda z ktorej vychádzajú všetky obrazovky
class AbstractScreen(Frame, ABC):
    def __init__(self, parent, controller, font_object):
        super().__init__(parent)

        self.controller = controller
        self.font = font_object
        self.populate_screen()

    @abstractmethod
    def populate_screen(self):
        pass

