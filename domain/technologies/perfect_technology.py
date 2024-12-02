
from domain.technologies.technology import Technology


class PerfectTechnology(Technology):
    @classmethod
    def name(cls):
        return 'PERFECT'

    def setup_technology_for_test(self, test_name):
        pass

    def setup_technology(self):
        pass

    def tear_down(self):
        pass

    def new_master_repository(self):
        pass

    def expose_http_interface(self, http_interface):
        pass
