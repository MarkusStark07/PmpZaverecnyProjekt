class Utils:
    @staticmethod
    def show_screen(app, screen_class):
        if app.current_screen is not None:
            app.current_screen.destroy()

        app.current_screen = screen_class(app.root, app)
        app.current_screen.pack(fill="both", expand=True)

    @staticmethod
    def go_back(self):
        from screens.main_screen import MainScreen

        Utils.show_screen(self.controller, MainScreen)