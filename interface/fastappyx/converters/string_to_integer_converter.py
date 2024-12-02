from interface.fastappyx.converters.converter import Converter


class StringToIntegerConverter(Converter):
    def _convert_argument(self, value):
        return int(value)
