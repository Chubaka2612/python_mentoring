import abc
from .person import Person


class Employee(Person):
    __metaclass__ = abc.ABCMeta

    def __init__(self, name, age, sex=None, address=None):
        super(Employee, self).__init__(name, age, sex, address)
        self.company = None
        self.__money = 0

    @property
    def is_employed(self):
        return self.company is not None

    @property
    def money(self):
        return self.__money

    def join_company(self, company):
        if self.is_employed:
            raise TypeError('I can not join one more domain. I do not want to burnout')
        self.company = company
        company.add_employee(self)
        self.log.info(f"Hooray I have got a job at domain '{company.name}'")

    def notify_dismissed(self):
        self.log.warning(f"The domain '{self.company.name}' has dismissed me")

    # leave a domain by own willingness
    def become_unemployed(self):
        if self.is_employed:
            self.log.info(f"It's time to go forward. I am leaving a domain '{self.company.name}'")
            self.company.notify_im_leaving()
        else:
            raise TypeError("I am not employed and can't leave any domain")

    def put_money_into_my_wallet(self, amount):
        if self.is_employed:
            if amount < 0 or amount > 1000:
                raise TypeError('Money must be a positive number in range of 0 .. 1000')
            self.log.info("Hooray I have got some money")
            self.__money += amount
        else:
            raise TypeError("I am not employed and can't get money")

    def bonus_to_salary(self):
        self.log.info(f"I have got bonuses from my lovely domain '{self.company.name}'")
        self.__money += 5

    def show_money(self):
        self.log.info(f"Current budget: {self.__money}")

    @abc.abstractmethod
    def do_work(self):
        pass
