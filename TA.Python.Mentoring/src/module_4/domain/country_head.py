from .log_configurator import get_logger

from .person import Person

log = get_logger('country_head')


def singleton(class_):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        else:
            log.info("CountryHead already exists")
        return instances[class_]

    return get_instance


@singleton
class CountryHead(Person):

    @staticmethod
    def sell_company(company):
        log.warning(f"Company '{company.name}' is to be sold")
        return company
