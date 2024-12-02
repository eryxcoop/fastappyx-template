from uuid import UUID

from interface.fastappyx.converters.converter import Converter


class StringToUUIDConverter(Converter):
    def _convert_argument(self, value):
        return UUID(value)
