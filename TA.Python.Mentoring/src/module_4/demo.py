from domain.company import Company
from domain.engineer import Engineer
from domain.country_head import CountryHead
from domain.log_configurator import get_logger

log = get_logger('demo')


def main():
    fruits_company = Company('Fruits', address='Ocean street, 1')
    print(fruits_company)

    # add some employees
    alex = Engineer('Alex', 55)
    alex.join_company(fruits_company)
    alex.do_work()
    alex.show_money()
    fruits_company.show_money()
    fruits_company.dismiss_employee(alex)
    fruits_company.go_bankrupt()
    fruits_company.make_a_party()

    vp = CountryHead("Alex", 23)
    log.info(vp)
    vp2 = CountryHead("Alex2", 33)
    log.info(vp2)


main()
