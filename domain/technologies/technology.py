from abc import abstractmethod, ABC


class Technology(ABC):
    @classmethod
    def is_for(cls, testing_technology):
        return testing_technology == cls.name()

    @classmethod
    @abstractmethod
    def name(cls):
        ...

    @abstractmethod
    def setup_technology_for_test(self, test_name):
        ...

    @abstractmethod
    def setup_technology(self):
        ...

    @abstractmethod
    def tear_down(self):
        ...

