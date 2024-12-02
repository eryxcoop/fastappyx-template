class HttpRequest:
    def __init__(self, webserver_request):
        self._webserver_request = webserver_request

    def headers(self):
        return self._webserver_request.headers

    def query_params(self):
        return self._webserver_request.query_params

    def path_params(self):
        return self._webserver_request.path_params

    async def json(self):
        return await self._webserver_request.json()

    async def form(self):
        return await self._webserver_request.form()
