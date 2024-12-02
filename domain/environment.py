from config_variables import DATABASE_TECHNOLOGY
from domain.application import Application
from domain.technologies.perfect_technology import PerfectTechnology
from domain.technologies.sqlalchemy_technology import XXXTechnology


class Environment:
    def __init__(self):
        self._application = None
        self._technology = None

    @classmethod
    def new_for_test(cls):
        environment = cls()
        environment.setup_technology_for_test()
        return environment

    @classmethod
    def new(cls):
        environment = cls()
        environment.setup_technology()
        return environment

    def technology(self):
        for technology in self.available_technologies():
            if technology.is_for(DATABASE_TECHNOLOGY):
                return technology()

        raise ValueError("Technology is not valid")

    def setup_technology_for_test(self):
        technology = self.technology()
        technology.setup_technology_for_test()
        self._technology = technology
        return self._technology

    def setup_technology(self):
        technology = self.technology()
        technology.setup_technology()
        self._technology = technology
        return self._technology

    def application(self):
        if self._application is None:
            self._application = self.create_application()
        return self._application

    def create_application(self):
        return Application.new_with(technology=self._technology)

    def available_technologies(self):
        return [PerfectTechnology, XXXTechnology]
