from constants import Constants
from domain.test import Test
from services.cipher_service import CipherService
from services.serial_interface_service import SerialInterfaceService
from services.storage.test_storage_service import TestStorageService

# Služba poskytujúca rozhranie na komunikáciu medzi hardwarovou službou, šifrovacou službou a grafickým rozhraním
class MessageService:

    @staticmethod
    def send(message):
        # šifrovanie zadanej správy
        encrypted_message = CipherService.encrypt(message)
        # zaslanie zašifrovanej správy na hardware
        if Constants.testMode == False:
            SerialInterfaceService().write(encrypted_message)
        # V prípade ak je aplikácia v testovacom móde sa zašifrovaná správa uloží do testovacieho úložiska
        else:
            TestStorageService().save(Test.TESTED_VALUE, encrypted_message)

    @staticmethod
    # Získanie šifrovanej správy z hardwaru
    def receive():
        if Constants.testMode == False:
            received_message = SerialInterfaceService().read()
        # V prípade ak je aplikácia v testovacom móde sa zašifrovaná správa vytiahne z testovacieho úložiska
        else:
            received_message = TestStorageService().get(Test.TESTED_VALUE)
        # Dešifrovanie správy
        decrypted_message = CipherService.decrypt(received_message)
        return decrypted_message