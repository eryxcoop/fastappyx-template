from typing import Any

from interface.fastappyx.errors import Error, FieldValidationError, ArgumentError


class Result:
    def __init__(self):
        self._object = {}
        self._errors = []

    def add_error(self, error: Error) -> None:
        self._errors.append(error)

    def add_field_errors(self, validation_error) -> None:
        for error in validation_error.errors():
            self.add_error(FieldValidationError(location=error["loc"][0], message=error["msg"]))

    def add_argument_error(self, argument_name: str, message) -> None:
        self._errors.append(ArgumentError(argument_name=argument_name, message=message))

    def add_simple_error(self, message: str) -> None:
        self._errors.append(Error("simple_error_code", message))

    def add_authentication_error(self, message: str) -> None:
        self._errors.append(Error("authentication_error", message))

    def add_not_found_error(self, message: str) -> None:
        self._errors.append(Error("not_found_error", message))

    def add_retry_error(self, message: str) -> None:
        self._errors.append(Error("retry_error", message))

    def get_errors(self) -> list[Error]:
        return self._errors

    def has_errors(self) -> bool:
        return len(self._errors) > 0

    def set_object(self, object) -> None:
        self._object = object

    def get_object(self) -> Any:
        return self._object
