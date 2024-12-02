class User:
    @classmethod
    def new_with(cls, name, email):
        return cls(name=name, email=email)

    def __init__(self, name, email):
        self._name = name
        self._email = email

    def has_email(self, potential_email):
        return self._email == potential_email
