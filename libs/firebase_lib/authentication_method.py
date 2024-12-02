class AuthenticationMethod:
    def decode_token(self, token):
        raise NotImplementedError("subclass responsibility")

    def account_id_from(self, decoded_token):
        raise NotImplementedError("subclass responsibility")
