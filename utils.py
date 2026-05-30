# Utils aplikácie
class Utils:
    # Zobrazenie novej obrazovky
    @staticmethod
    def show_screen(app, screen_class, font_object):
        # Ak už existuje v okne nejaká zobrazená obrazovka zničí ju
        if app.current_screen is not None:
            app.current_screen.destroy()

        # Vloží do  okna novú obrazovku
        app.current_screen = screen_class(app.root, app, font_object)
        app.current_screen.pack(fill="both", expand=True)

    # Vrátenie sa na hlavnú obrazovku
    @staticmethod
    def go_back_to_main_screen(self):
        # Musíme lokálne importovať hlavnú obrazovku kvôli zabráneniu cyklickým importom
        # Keby xScreen importoval MainScreen kvôli využitiu show_screen vznikla by slučka
        # main_screen.py importuje x_screen a ten spätne importuje main_screen.py
        # Pythno v danom momente ale ešte nedokončil inicializáciu triedy MainScreen, takže by to skončilo chybou
        # Lokálny import vnútri metódy sa vykoná za behu, to zabezpečí že sú obe triedy kompletne načítané
        from screens.main_screen import MainScreen

        # Zobrazenie hlavnej obrazovky
        Utils.show_screen(self.controller, MainScreen, self.font)