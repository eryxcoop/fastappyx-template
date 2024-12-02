from domain.repositories.master_transient_repository import MasterTransientRepository
from domain.technologies.technology import Technology


class PerfectTechnology(Technology):
    @classmethod
    def name(cls):
        return 'PERFECT'

    def setup_technology_for_test(self):
        pass

    def setup_technology(self):
        pass

    def tear_down(self):
        pass

    def new_master_repository(self):
        return MasterTransientRepository()

    def expose_http_interface(self, http_interface):
        pass
