from interface.fastappyx.converters.converter import Converter


class ListIdConverter(Converter):
    def __init__(self, argument_name, interface_id_converter):
        super().__init__(argument_name)
        self._id_converter = interface_id_converter

    def _convert_argument(self, value):
        return [self._id_converter.internal_id_for(v) for v in value]
