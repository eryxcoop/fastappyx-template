class HttpSimpleParameter:
    def __init__(self, name, location):
        self._name = name
        self._location = location

    async def get_argument_from_request(self, request):
        raw_data = await self._location.get_argument_data_from_request(request)
        return raw_data.get(self.name())

    def name(self):
        return self._name
