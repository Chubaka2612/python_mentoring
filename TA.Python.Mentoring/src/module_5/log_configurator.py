import sys
import logging


def get_logger(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(name)s - %(message)s')

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)
    return log