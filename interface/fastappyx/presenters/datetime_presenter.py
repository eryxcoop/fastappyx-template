from interface.fastappyx.presenters.base_presenter import BasePresenter


class DatetimePresenter(BasePresenter):
    def present(self):
        return self._result_object.isoformat() if self._result_object else None
