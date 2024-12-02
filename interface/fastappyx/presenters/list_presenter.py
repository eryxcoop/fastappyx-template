from interface.fastappyx.presenters.base_presenter import BasePresenter


class ListPresenter(BasePresenter):
    def __init__(self, object_presenter, objects_list, business, interface, name: str = None, extra_params=None):
        super().__init__(objects_list, interface, business)
        self._object_presenter = object_presenter
        self._name = name
        self._extra_params = extra_params or {}

    def object_name(self) -> str | None:
        return self._name

    def present(self):
        objects_list = self._result_object
        return [
            self._object_presenter(object, self._interface, self._business, **self._extra_params).present()
            for object in objects_list
        ]
