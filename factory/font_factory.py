import tkinter.font as tkFont

class FontFactory:
    # Konštruktor objektu Font
    def __init__(self, family, size):
        self.family = family
        self.size = size

    # vracia pre apku default font
    def app_default(self):
        return tkFont.Font(family=self.family, size=self.size)

    # vracia pre apku default font s inou veľkosťou
    def custom_size(self, size):
        return tkFont.Font(family=self.family, size=size)

    # vracia pre apku default font s inou family
    def custom_family(self, family):
        return tkFont.Font(family=family, size=self.size)

    # vracia úplne custom font
    def custom(self, family, size):
        return tkFont.Font(family=family, size=size)