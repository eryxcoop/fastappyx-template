from interface.fastappyx.http_request import HttpRequest


class RequestQueryParamLocation:
    async def get_argument_data_from_request(self, request: HttpRequest):
        return request.query_params()
