import pytest
import cityCafes


@pytest.fixture(params=[{'name': 'Cafe Jumping Bean',
                          'opening_hours': {'weekday_text': [], 'open_now': True},
                          'vicinity': '1401 West Taylor Street, Chicago'}])
def open_place(request):
    return request.param


@pytest.fixture(params=[{'name': 'Stax Cafe',
                          'opening_hours': {'weekday_text': [], 'open_now': False},
                          'vicinity': '1401 West Taylor Street, Chicago'}])
def closed_place(request):
    return request.param


def test_get_open_now(open_place):
    """
    Positive test for get_open_now method
    :param open_place: pytest.fixture of a place that is opened.
    """
    print_statement = cityCafes.get_open_now(open_place)
    assert print_statement == "Cafe Jumping Bean, 1401 West Taylor Street, Chicago"


def test_get_open_negative(closed_place):
    """
    Negative test for get_open_now method
    :param closed_place: pytest.fixture of a place that is closed.
    """
    print_statement = cityCafes.get_open_now(closed_place)
    assert print_statement == "Stax Cafe is closed."