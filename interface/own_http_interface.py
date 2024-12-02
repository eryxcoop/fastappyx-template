from interface.fastappyx.http_interface import HttpInterface


# Rename this class to match application name
class OwnHttpInterface(HttpInterface):
    def __init__(self, application, id_converter):
        super().__init__(application)

        self._application = application
        self._id_converter = id_converter

    def endpoints(self):
        return []
