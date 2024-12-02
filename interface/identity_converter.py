from cryptography.fernet import InvalidToken

from errors.element_not_found import ElementNotFound
from libs.id_encrypter import IdEncrypter


class IdentityIdConverter:
    def __init__(self, key: str):
        # key must be generated using Fernet.generate_key().decode()
        self._id_encrypter = IdEncrypter(key)

    def external_id_for(self, an_object, an_object_repository) -> str:
        object_id = an_object_repository.id_of(an_object)
        return self._id_encrypter.encrypt(object_id)

    def internal_id_for(self, external_id: str) -> int:
        try:
            return self._id_encrypter.decrypt(external_id)
        except InvalidToken:
            raise ElementNotFound("Invalid external id")
