import pytest

from domain.environment import Environment


@pytest.fixture()
def test_application():
    application = Environment.new_for_test().application()

    yield application

@pytest.fixture
def business(test_application):
    return test_application.current_business()


def test_create_user(business):
    business.create_user(name="Delfi Brea", email="delfi@brea.com")

    assert business.has_user_with_email("delfi@brea.com")


def test_create_more_than_one_user(business):
    business.create_user(name="Delfi Brea", email="delfi@brea.com")
    business.create_user(name="Bea Gonzalez", email="bea@gonzalez.com")

    assert business.has_n_users(2)
    assert business.has_user_with_email("delfi@brea.com")
    assert business.has_user_with_email("bea@gonzalez.com")