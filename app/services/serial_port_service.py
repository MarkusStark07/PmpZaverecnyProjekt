import serial

from app.domain.config import Config
from app.services.singleton_service import SingletonService
from app.services.storage.config_storage_service import ConfigStorageService

# Služba komunikácie na seriovom interfacom
class SerialPortService(SingletonService):
    # Inicializácia spojenia na základe nastavených parametrov uložený v configuračnom úložisku
    def __init__(self):
        # Kontrola či už má objekt vytvorené sériové spojenie
        if not hasattr(self, "serial_connection"):
            port = ConfigStorageService().get(Config.SERIAL_PORT)
            speed = ConfigStorageService().get(Config.SERIAL_SPEED)
            if port == "" or speed == "":
                raise Exception("Sériový port alebo rýchlosť neboli nastavené!")
            self.serial_connection = serial.Serial(str(port), int(speed), timeout=0.1)

    # čítanie dát zo sériového spojenia
    def read(self):
        while True:
            # kontrola či sú dostupné nejaké dáta na čítanie
            if self.serial_connection.in_waiting > 0:
                raw_data = self.serial_connection.readline()
                # prevod do textovej formy
                return raw_data.decode("utf-8")

    # písanie dát do sériového spojenia
    def write(self, data):
        # pridanie znaku nového riadku na koniex správy
        data = data + "\n"
        # prevod na bajty
        self.serial_connection.write(data.encode("utf-8"))