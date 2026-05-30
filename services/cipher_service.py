from domain.config import Config
from services.storage.config_storage_service import ConfigStorageService


class CipherService:

    @staticmethod
    def _get_key_bytes():
        key = ConfigStorageService().get(Config.ENCRYPTION_KEY)
        if key == "":
            raise Exception("Encryption key is not set")
        return key.encode("utf-8")

    @staticmethod
    def xor_cipher(data):
        key = CipherService._get_key_bytes()
        len_key = len(key)
        encoded = []

        for i in range(len(data)):
            encoded.append(data[i] ^ key[i % len_key])

        return bytes(encoded)

    @staticmethod
    def encrypt(message):
        message_bytes = message.encode("utf-8")
        encrypted_bytes = CipherService.xor_cipher(message_bytes)
        return encrypted_bytes.hex()

    @staticmethod
    def decrypt(encrypted_message):
        encrypted_bytes = bytes.fromhex(encrypted_message)
        decrypted_bytes = CipherService.xor_cipher(encrypted_bytes)
        return decrypted_bytes.decode("utf-8")