class BasePresenter:
    def __init__(self, result_object, interface=None, business=None):
        self._result_object = result_object
        self._interface = interface
        self._business = business

    def object_name(self) -> str | None:
        return None

    def present(self):
        return self._result_object

    def present_with_name(self):
        return {self.object_name(): self.present()} if self.object_name() else self.present()

    def external_id_for(self, an_object):
        object_repository = self._business.master_repository().notebooks_repository()
        external_id = self._interface.id_converter().external_id_for(an_object, object_repository)
        return external_id
