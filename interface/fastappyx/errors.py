class Error:
    def __init__(self, code, message):
        self._code = code
        self._message = message

    def code(self):
        return self._code

    def message(self):
        return self._message


class FieldValidationError(Error):
    def __init__(self, message, location):
        super().__init__("field_validation_error", message)
        self._location = location

    def location(self):
        return self._location


class ArgumentError(Error):
    def __init__(self, argument_name, message):
        super().__init__("argument_error", message)
        self._argument_name = argument_name

    def argument_name(self):
        return self._argument_name
