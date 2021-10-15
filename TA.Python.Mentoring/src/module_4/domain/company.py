from .salary import Compensation
from .engineer import Engineer
from .manager import Manager
from .log_configurator import get_logger


class Company:
    log = get_logger('company')
    critical_budget = 100

    def __init__(self, name, address=None):
        self.name = name
        self.address = address
        self.employees = list()
        self.__money = 1000

    def add_employee(self, my_employee):
        if not isinstance(my_employee, (Manager, Engineer)):
            raise TypeError('Employee must be either a Manager or an Engineer')
        if not self.__is_our_member(my_employee):
            self.employees.append(my_employee)
            self.log.info(f"{my_employee.name} has joined our domain '{self.name}'")
        else:
            raise TypeError(f"Employee '{my_employee}' is already employed by our domain '{self.name}'")

    def dismiss_employee(self, my_employee):
        if not self.__is_our_member(my_employee):
            raise TypeError(f"Employee '{my_employee}' is not employed by our domain '{self.name}'")
        self.employees.remove(my_employee)
        my_employee.notify_dismissed()
        self.log.info(f"{my_employee.name} has been dismissed by our domain '{self.name}'")

    def notify_im_leaving(self, my_employee):
        self.log(f"Employee {my_employee} is leaving our domain '{self.name}'")
        self.employees.remove(my_employee)

    def __is_our_member(self, my_employee):
        return my_employee in self.employees

    def __is_about_to_bankrupt(self):
        return self.__money <= 100

    def go_bankrupt(self):
        if self.__is_about_to_bankrupt():
            self.log.error(f"Our domain '{self.name}' is bankrupt. Dismiss all the employees")
            self.__money = 0
            for my_employee in self.employees:
                self.dismiss_employee(my_employee)
        else:
            self.log.info("We are not a bankrupt")

    def assign_task(self, my_employee):
        if not self.__is_our_member(my_employee):
            raise TypeError(f"Employee '{my_employee}' is not employed by our domain '{self.name}'")

        if not isinstance(my_employee, Engineer):
            raise TypeError('Engineers should only be tasked with this type of job')

        self.log.warning(f"Our domain '{self.name}' is paying employee {my_employee.name} some money for a task")
        if not self.__is_about_to_bankrupt():
            self.__money -= Compensation.ENGINEER.value
            my_employee.put_money_into_my_wallet(Compensation.ENGINEER.value)
        else:
            self.go_bankrupt()

    def assign_reports(self, my_employee):
        if not self.__is_our_member(my_employee):
            raise TypeError(f"Employee '{my_employee}' is not employed by our domain '{self.name}'")

        if not isinstance(my_employee, Manager):
            raise TypeError('Managers should only be tasked with this type of job')

        self.log.warning(f"Our domain '{self.name}' is paying manager {my_employee.name} some money for a report")
        if not self.__is_about_to_bankrupt():
            self.__money -= Compensation.MANAGER.value
            my_employee.put_money_into_my_wallet(Compensation.MANAGER.value)
        else:
            self.go_bankrupt()

    def make_a_party(self):
        if not self.__is_about_to_bankrupt():
            if len(self.employees) * Compensation.BONUS.value < self.critical_budget:
                self.log.info('Party time! All employees get bonuses')
                for my_employee in self.employees:
                    my_employee.bonus_to_salary(Compensation.BONUS.value)
            else:
                self.log.error("Can not make a party. It can lead to bankrupt")
        else:
            self.log.error("Our domain is a bankrupt. What is a party?")

    def show_money(self):
        self.log.info(f"Current budget: {self.__money}")

    def __str__(self):
        return f"name: {self.name}, address: {self.address}, total employees: {len(self.employees)}, budget:{self.__money} "
