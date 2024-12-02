from interface.fastappyx.authenticators.http_authenticator import HttpAuthenticator


class NoAuthenticator(HttpAuthenticator):
    async def authenticate(self, request, gatekeeper):
        return None
