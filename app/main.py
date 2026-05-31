from tkinter import *

from constants import Constants
from factory.font_factory import FontFactory
from screens.main_screen import MainScreen
from utils import Utils


class Main:
    # Initializuje okno
    def __init__(self):
        self.root = Tk()
        self.root.title(Constants.windowTitle)
        self.root.geometry(Constants.windowSize)

        # Zobrazí main screens
        self.current_screen = None
        Utils.show_screen(self, MainScreen, FontFactory(Constants.defaultFont, Constants.defaultFontSize))

    # Spustí aplikaciu
    def run(self):
        self.root.mainloop()

app = Main()
app.run()