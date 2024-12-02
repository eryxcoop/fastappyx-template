from interface.fastappyx.http_request import HttpRequest


class RequestFormParamLocation:
    async def get_argument_data_from_request(self, request: HttpRequest):
        return await request.form()
