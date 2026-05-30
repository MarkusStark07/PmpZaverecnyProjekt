# Singleton služba zabezpečuje vytvorenie iba jednej inštancie daného objekta
class SingletonService:
    # Dictionary ktorý si uchováva jednotlivé inštancie
    _instances = {}

    # vytvorenie novej inštancie objektu
    def __new__(cls, *args, **kwargs):
        # táto podmienka zabezpečí vytvorenie inštancie iba v prípade ak neexistuje
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonService, cls).__new__(cls)
        # vráteenie už existujúcej alebo vytvorenej inštancie
        return cls._instances[cls]