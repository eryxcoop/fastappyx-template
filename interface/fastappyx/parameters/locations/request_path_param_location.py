from interface.fastappyx.http_request import HttpRequest


class RequestPathParamLocation:
    async def get_argument_data_from_request(self, request: HttpRequest):
        return request.path_params()
