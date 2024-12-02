class HttpSchemaParameter:
    def __init__(self, name, schema, location):
        self._name = name
        self._schema = schema
        self._location = location

    async def get_argument_from_request(self, request):
        raw_data = await self._location.get_argument_data_from_request(request)
        return self._schema(**raw_data)

    def name(self):
        return self._name
