import pytest

from domain.environment import Environment


@pytest.fixture()
def test_application():
    application = Environment.new().application()

    yield application


@pytest.fixture
def business(test_application):
    return test_application.current_business()


def test_example(business):
    business.do_something()

    assert business.is_something_done()