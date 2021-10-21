from abc import ABC
from .log_configurator import get_logger
from .gender import Sex


class Person(ABC):
    log = get_logger('person')

    def __init__(self, name, age, sex=None, address=None):
        self.name = name
        self.__age = age
        self.__sex = sex
        self.address = address

    # @abstractmethod
    # def show_info(self):
    #     pass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            raise ValueError('Age must be in range 1 .. 100')

    @property
    def sex(self):
        return self.__sex

    @sex.setter
    def sex(self, sex):
        if sex is not None:
            if not isinstance(sex, Sex):
                raise TypeError('Sex must be an instance of Sex Enum')
        self.__sex = sex

    def __eq__(self, obj):
        return isinstance(obj, Person) and (self.name, self.sex, self.address, self.age) \
               == (obj.name, obj.__sex, obj.address, obj.age)

    def __str__(self):
        return f"name: {self.name}, age: {self.__age}, sex: {self.__sex}, address: {self.address}"
