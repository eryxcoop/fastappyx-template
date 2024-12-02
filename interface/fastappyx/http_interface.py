from abc import ABC, abstractmethod

from interface.fastappyx.endpoint import Endpoint


class HttpInterface(ABC):
    def __init__(self, application):
        self._application = application

    def new_endpoint(self, method, path, handler_class, authenticator=None, is_async=False):
        return Endpoint(
            application=self._application,
            method=method,
            path=path,
            is_async=is_async,
            handler_class=handler_class,
            authenticator=authenticator,
            interface=self,
        )

    @abstractmethod
    def endpoints(self): ...
