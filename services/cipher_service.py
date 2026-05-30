from domain.config import Config
from services.storage.config_storage_service import ConfigStorageService

# Služba šifrovania a dešifrovania správ pomocou XOR šifry
class CipherService:

    # Táto metóda získa klúč z configuračného úložiska validuje ho
    @staticmethod
    def _get_key_bytes():
        key = ConfigStorageService().get(Config.ENCRYPTION_KEY)
        # Validovanie klúča, ide o obyčajnú kontrolu či bol klúč uložený
        if key == "":
            raise Exception("Encryption key is not set")
        return key.encode("utf-8")

    # XOR šifra
    @staticmethod
    def xor_cipher(data):
        encoded = []

        # získanie klúča a jeho dĺžky.
        key = CipherService._get_key_bytes()
        len_key = len(key)

        # Iterácia cez každý bajt vložených dát
        for i in range(len(data)):
            # samotná logika xor šifrovania
            # pre každý bajt dát a klúča robíme XOR operáciu, jej výsledný bajt ukladáme do zoznamu encoded
            # modulo pri klúči nám zabezpečí že ak by bol klúč menší než dáta tak sa po dosiahnutý koncu klúča index vráti na začiatok
            encoded.append(data[i] ^ key[i % len_key])

        # vrátenie výsledku ako bytes
        return bytes(encoded)

    # šifrovanie správy
    @staticmethod
    def encrypt(message):
        # Prevod textu na bytes
        message_bytes = message.encode("utf-8")
        # šifrovanie
        encrypted_bytes = CipherService.xor_cipher(message_bytes)
        # vrátanie výsledku v hexadecimálnom formáte
        return encrypted_bytes.hex()

    # dešifrovanie správy
    @staticmethod
    def decrypt(encrypted_message):
        # Prevod hexadecimálnej formy šifrovaného textu na bytes
        encrypted_bytes = bytes.fromhex(encrypted_message)
        # dešifrovanie
        decrypted_bytes = CipherService.xor_cipher(encrypted_bytes)
        # vrátenie výsledku v textovej forme
        return decrypted_bytes.decode("utf-8")