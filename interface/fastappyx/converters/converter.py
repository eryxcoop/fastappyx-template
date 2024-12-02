from abc import ABC, abstractmethod

from errors.element_not_found import ElementNotFound


class Converter(ABC):
    def __init__(self, argument_name):
        self._argument_name = argument_name

    def applies_to(self, argument_name):
        return self._argument_name == argument_name

    def convert(self, arguments, result):
        value = arguments[self._argument_name]

        try:
            arguments[self._argument_name] = self._convert_argument(value)
        except ElementNotFound:
            result.add_not_found_error("Element not found.")
        except Exception as e:
            result.add_argument_error(self._argument_name, str(e))

    @abstractmethod
    def _convert_argument(self, value): ...
