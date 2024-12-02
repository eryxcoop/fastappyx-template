from interface.fastappyx.presenters.base_presenter import BasePresenter


class DatePresenter(BasePresenter):
    def present(self):
        return self._result_object.strftime("%Y-%m-%d") if self._result_object else None
