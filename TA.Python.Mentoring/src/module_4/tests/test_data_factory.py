import faker

from ..domain.gender import Sex
from ..domain.person import Person
from ..domain.engineer import Engineer
from ..domain.company import Company

FAKE = faker.Faker()


def get_valid_person():
    name = FAKE.first_name_nonbinary()
    address = FAKE.street_address()
    age = FAKE.pyint(1, 100)

    sex = Sex.get_gender()
    return Person(name, age, sex, address)


def get_valid_engineer():
    name = FAKE.first_name_nonbinary()
    address = FAKE.street_address()
    age = FAKE.pyint(1, 100)
    sex = Sex.get_gender()
    return Engineer(name, age, sex, address)


def get_valid_company():
    name = FAKE.catch_phrase()
    address = FAKE.street_address()
    return Company(name, address)
