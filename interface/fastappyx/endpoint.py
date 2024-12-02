from interface.fastappyx.authenticators.no_authenticator import NoAuthenticator


class Endpoint:
    GET_METHOD = "GET"
    POST_METHOD = "POST"
    DELETE_METHOD = "DELETE"
    PUT_METHOD = "PUT"
    PATCH_METHOD = "PATCH"

    def __init__(self, application, method, path, handler_class, interface, is_async=True, authenticator=None):
        self._application = application
        self._method = method
        self._path = path
        self._handler_class = handler_class
        self._is_async = is_async
        self._interface = interface
        self._authenticator = authenticator or NoAuthenticator()

    def is_get(self):
        return self._method == self.GET_METHOD

    def is_post(self):
        return self._method == self.POST_METHOD

    def is_delete(self):
        return self._method == self.DELETE_METHOD

    def is_put(self):
        return self._method == self.PUT_METHOD

    def is_patch(self):
        return self._method == self.PATCH_METHOD

    def path(self):
        return self._path

    def handler(self, task_queue=None):
        return self._handler_class(
            application=self._application, authenticator=self.authenticator(), task_queue=task_queue, interface=self._interface
        )

    def authenticator(self):
        return self._authenticator

    def is_async(self):
        return self._is_async
