from config_variables import CONVERTION_KEY_HTTP_INTERFACE
from domain.business import Business
from interface.identity_converter import IdentityIdConverter
from interface.own_http_interface import OwnHttpInterface
from libs.time_lib.clock import Clock


class Application:
    @classmethod
    def new_with(cls, technology):
        return cls(technology=technology, authentication_method=None)

    def __init__(self, technology, authentication_method):
        self._clock = Clock()
        self._technology = technology
        self._authentication_method = authentication_method
        self._business = self._create_business(
            master_repository=self._technology.new_master_repository(), authentication_method=self._authentication_method
        )
        self._use_http_interface()

    def http_interface(self):
        return self._http_interface

    def storage(self):
        return self._technology

    def webserver(self):
        return self._technology.webserver()

    def authentication_method(self):
        return self._authentication_method

    def current_business(self):
        return self._business

    def get_new_business(self, session):
        master_repository = self._technology.new_master_repository(session)
        return Business(
            master_repository=master_repository,
            authentication_method=self._authentication_method,
            clock=self.clock(),
        )

    def clock(self):
        return self._clock

    def _create_business(self, master_repository, authentication_method):
        firebase_authentication_method = authentication_method
        return Business(
            master_repository=master_repository,
            authentication_method=firebase_authentication_method,
            clock=self.clock(),
        )

    def _use_http_interface(self):
        id_converter = IdentityIdConverter(key=CONVERTION_KEY_HTTP_INTERFACE)

        self._http_interface = OwnHttpInterface(application=self, id_converter=id_converter)
        self._technology.expose_http_interface(self._http_interface)
