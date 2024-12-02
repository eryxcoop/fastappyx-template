class ResultPresenter:
    def __init__(self, result, object_presenter):
        self._result = result
        self._object_presenter = object_presenter

    def present(self):
        if self._result.has_errors():
            return self._present_failed_result()
        present_object = self._object_presenter.present_with_name()
        return self._presented_result(present_object=present_object)

    def _present_failed_result(self):
        presented_errors = [self._present_error(error) for error in self._result.get_errors()]
        return self._presented_result(errors=presented_errors)

    def _presented_result(self, present_object=None, errors=None):
        return {"object": present_object or {}, "errors": errors or []}

    def _present_error(self, error):
        if error.code() == "field_validation_error":
            return {"code": error.code(), "field": error.location(), "message": error.message()}
        if error.code() == "argument_error":
            return {"code": error.code(), "argument": error.argument_name(), "message": error.message()}
        return {"code": error.code(), "message": error.message()}
