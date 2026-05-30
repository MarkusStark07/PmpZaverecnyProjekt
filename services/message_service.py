from constants import Constants
from domain.test import Test
from services.cipher_service import CipherService
from services.serial_port_service import SerialPortService
from services.storage.test_storage_service import TestStorageService


class MessageService:

    @staticmethod
    def send(message):
        encrypted_message = CipherService.encrypt(message)
        if Constants.testMode == False:
            SerialPortService().write(encrypted_message)
        else:
            TestStorageService().save(Test.TESTED_VALUE, encrypted_message)

    @staticmethod
    def receive():
        if Constants.testMode == False:
            received_message = SerialPortService().read()
        else:
            received_message = TestStorageService().get(Test.TESTED_VALUE)
        decrypted_message = CipherService.decrypt(received_message)
        return decrypted_message