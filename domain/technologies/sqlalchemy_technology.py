from domain.technologies.technology import Technology
from interface.fastappyx.fast_api_interface_adapter import FastApiInterfaceAdapter
from fastapi import FastAPI

class XXXTechnology(Technology):
    @classmethod
    def name(cls):
        return 'SQLALCHEMY'

    def setup_technology_for_test(self, test_name):
        pass

    def setup_technology(self):
        self._webserver = FastAPI()

    def tear_down(self):
        pass

    def new_master_repository(self):
        pass

    def interfaces(self):
        pass

    def webserver(self):
        return self._webserver

    def expose_http_interface(self, http_interface):
        FastApiInterfaceAdapter(self._webserver, http_interface).adapt_endpoints()


