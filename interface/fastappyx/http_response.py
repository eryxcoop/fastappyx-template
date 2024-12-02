class HttpResponse:
    def __init__(self, status_code, content):
        self._status_code = status_code
        self._content = content

    def status_code(self):
        return self._status_code

    def content(self):
        return self._content
