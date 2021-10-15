import pytest

from .test_data_factory import get_valid_person


@pytest.mark.smoke
def test_when_valid_data_provided_then_person_created():
    test_person = get_valid_person()
    assert test_person.name is not None, "Name is not None"
    assert test_person.age is not None, "Age is not None"
    assert test_person.sex is not None, "Gender is not None"
    assert test_person.address is not None, "Address is not None"


@pytest.mark.regression
def test_when_invalid_sex_provided_then_error_occurred():
    test_person = get_valid_person()
    with pytest.raises(TypeError):
        test_person.sex = "INVALID"


@pytest.fixture(scope="function", params=[0, 101])
def invalid_age_param(request):
    return request.param


@pytest.mark.smoke
def test_when_invalid_age_provided_then_error_occurred(invalid_age_param):
    test_person = get_valid_person()
    with pytest.raises(TypeError):
        test_person.age = invalid_age_param


@pytest.fixture(scope="function", params=[1, 55, 10])
def valid_age_param(request):
    return request.param


@pytest.mark.regression
def test_when_valid_age_provided_then_no_error_occurred(valid_age_param):
    test_person = get_valid_person()
    test_person.age = valid_age_param
