import anyio
from fastapi import Request, Response, BackgroundTasks

from interface.fastappyx.http_request import HttpRequest


class FastApiInterfaceAdapter:
    def __init__(self, fast_api_webserver, http_interface):
        self._http_interface = http_interface
        self._fast_api_webserver = fast_api_webserver

    def adapt_endpoints(self):
        for endpoint in self._http_interface.endpoints():
            if endpoint.is_get():
                self._add_generic_get_endpoint(endpoint)
            elif endpoint.is_post():
                self._add_generic_post_endpoint(endpoint)
            elif endpoint.is_put():
                self._add_generic_put_endpoint(endpoint)
            elif endpoint.is_delete():
                self._add_generic_delete_endpoint(endpoint)
            elif endpoint.is_patch():
                self._add_generic_patch_endpoint(endpoint)
            else:
                raise ValueError(f"Unsupported method {endpoint.method()}")

    def _add_generic_get_endpoint(self, endpoint):
        self._fast_api_webserver.get(endpoint.path())(self._fast_api_handler(endpoint))

    def _add_generic_post_endpoint(self, endpoint):
        self._fast_api_webserver.post(endpoint.path())(self._fast_api_handler(endpoint))

    def _add_generic_put_endpoint(self, endpoint):
        self._fast_api_webserver.put(endpoint.path())(self._fast_api_handler(endpoint))

    def _add_generic_patch_endpoint(self, endpoint):
        self._fast_api_webserver.patch(endpoint.path())(self._fast_api_handler(endpoint))

    def _add_generic_delete_endpoint(self, endpoint):
        self._fast_api_webserver.delete(endpoint.path())(self._fast_api_handler(endpoint))

    def _async_fastapi_handler(self, endpoint):
        async def handler(request: Request, response: Response, background_tasks: BackgroundTasks):
            http_request = HttpRequest(request)
            handler_response = await endpoint.handler().handle(http_request)
            response.status_code = handler_response.status_code()
            return handler_response.content()

        return handler

    def _sync_fastapi_handler(self, endpoint):
        def handler(request: Request, response: Response):
            http_request = HttpRequest(request)
            handler_response = anyio.run(endpoint.handler().handle, http_request)
            response.status_code = handler_response.status_code()
            return handler_response.content()

        return handler

    def _fast_api_handler(self, endpoint):
        if endpoint.is_async():
            return self._async_fastapi_handler(endpoint)
        return self._sync_fastapi_handler(endpoint)
