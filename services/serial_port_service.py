import serial

from domain.config import Config
from services.singleton_service import SingletonService
from services.storage.config_storage_service import ConfigStorageService


class SerialPortService(SingletonService):
    def __init__(self):
        if not hasattr(self, "serial_connection"):
            interface = ConfigStorageService().get(Config.SERIAL_INTERFACE)
            port = ConfigStorageService().get(Config.SERIAL_PORT)
            self.serial_connection = serial.Serial(str(interface), int(port), timeout=0.1)

    def read(self):
        if self.serial_connection.in_waiting > 0:
            raw_data = self.serial_connection.readline()
            return raw_data.decode("utf-8")
        return None

    def write(self, data):
        data = data + "\n"
        self.serial_connection.write(data.encode("utf-8"))