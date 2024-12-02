class WebsocketEndpoint:
    def __init__(self, application, broadcaster, path, handler_class):
        self._application = application
        self._broadcaster = broadcaster
        self._path = path
        self._handler_class = handler_class

    def path(self):
        return self._path

    def handler(self):
        return self._handler_class(application=self._application, broadcaster=self._broadcaster)
