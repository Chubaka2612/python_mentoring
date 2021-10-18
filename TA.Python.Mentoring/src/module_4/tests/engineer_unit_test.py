import pytest

from .test_data_factory import get_valid_engineer
from .test_data_factory import get_valid_company


# pytest --strict -m smoke --html=report.html --self-contained-html
@pytest.mark.smoke
def test_when_new_engineer_created_then_no_money_and_no_company_has():
    test_engineer = get_valid_engineer()
    assert test_engineer.name is not None, "Name is not None"
    assert test_engineer.age is not None, "Age is not None"
    assert test_engineer.sex is not None, "Gender is not None"
    assert test_engineer.address is not None, "Address is not None"
    assert test_engineer.company is None, "Company is None"
    assert test_engineer.money == 0, "Engineer has no money"


@pytest.mark.regression
def test_when_engineer_joined_new_company_then_they_got_employed():
    test_company = get_valid_company()
    test_engineer = get_valid_engineer()
    test_engineer.join_company(test_company)
    assert test_engineer.company == test_company, "Company is not None"
    assert test_engineer.is_employed, "Engineer is employed"


@pytest.mark.smoke
def test_when_engineer_joined_company_then_they_are_not_able_to_join_one_more():
    test_company = get_valid_company()
    test_company2 = get_valid_company()
    test_engineer = get_valid_engineer()
    test_engineer.join_company(test_company)
    with pytest.raises(ValueError):
        test_engineer.join_company(test_company2)


@pytest.mark.smoke
@pytest.mark.parametrize("money", [-10, 1001])
def test_when_engineer_got_invalid_money_then_error_is_occurred(money):
    test_engineer = get_valid_engineer()
    test_company = get_valid_company()
    test_engineer.join_company(test_company)
    with pytest.raises(ValueError):
        test_engineer.put_money_into_my_wallet(money)
