import time
from module_5.log_configurator import get_logger

log = get_logger('timer')


class TimerError(Exception):
    pass


class Timer:

    def __init__(self):
        self._start_time = None

    def start(self):
        if self._start_time is not None:
            raise TimerError(f"Тimer is already working. Use .stop() to stop it")
        self._start_time = time.perf_counter()

    def stop(self):
        if self._start_time is None:
            raise TimerError(f"Timer is not working. Use .start() to start it")
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        log.info(f"Calculation takes {elapsed_time:0.4f} sec")
