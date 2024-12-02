class AuthenticationError(Exception):
    @classmethod
    def for_invalid_token(cls):
        return cls("Invalid token")

    @classmethod
    def for_missing_token(cls):
        return cls("Missing token")
