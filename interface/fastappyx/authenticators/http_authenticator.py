from abc import ABC


class HttpAuthenticator(ABC):
    def authenticate(self, request, gatekeeper): ...
