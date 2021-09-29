import sys
import logging


def get_logger(name, file_level, console_level, file='log/log.txt'):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s | %(levelname)-8s | %(name)s - %(message)s')

    file_handler = logging.FileHandler(file)
    file_handler.setLevel(file_level.upper())
    file_handler.setFormatter(formatter)
    log.addHandler(file_handler)

    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_handler.setLevel(console_level.upper())
    console_handler.setFormatter(formatter)
    log.addHandler(console_handler)
    return log
