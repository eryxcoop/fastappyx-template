from cryptography.fernet import Fernet


class IdEncrypter:
    def __init__(self, key: str = None):
        self._key = key.encode() if key else Fernet.generate_key()

    def encrypt(self, an_id: int) -> str:
        encryption = Fernet(self._key).encrypt(str(an_id).encode("utf-8")).decode("utf-8")
        return str(encryption)

    def decrypt(self, encrypted_id: str) -> int:
        decrypted_id_bytes = Fernet(self._key).decrypt(encrypted_id.encode("utf-8"))
        return int(decrypted_id_bytes.decode("utf-8"))
