from fastapi.websockets import WebSocket


class FastApiWebsocketInterfaceAdapter:
    def __init__(self, fast_api_webserver, websocket_interface, application):
        self._websocket_interface = websocket_interface
        self._fast_api_webserver = fast_api_webserver
        self._application = application

    def adapt_endpoints(self):
        for endpoint in self._websocket_interface.endpoints():
            self._add_websocket_endpoint(endpoint)

    def _add_websocket_endpoint(self, endpoint):
        self._fast_api_webserver.websocket(endpoint.path())(self._fast_api_websocket_handler(endpoint))

    def _fast_api_websocket_handler(self, endpoint):
        async def handler(websocket: WebSocket, user_token: str):
            await endpoint.handler().handle(websocket, user_token)

        return handler
