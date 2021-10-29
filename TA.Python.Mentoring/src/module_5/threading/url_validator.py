from queue import Queue
from threading import Thread
import requests
from status_code import Status
from url_result import UrlResult
from module_5.log_configurator import get_logger

log = get_logger('url_validator')


def validate_url_and_write(q, result):
    while not q.empty():
        work = q.get()
        try:
            status = requests.get(work[1]).status_code
            is_ok = status == Status.OK
            url_result = UrlResult(work[1], is_ok, status)
        except:
            url_result = UrlResult(work[1], False, None)
        log.info("Processing:" + str(url_result))
        result[work[0]] = url_result
        q.task_done()


def validate_urls(urls):
    q = Queue(maxsize=0)
    num_threads = min(50, len(urls))
    results = [{} for _ in urls]
    for i in range(len(urls)):
        q.put((i, urls[i]))

    for i in range(num_threads):
        print('Starting thread ', i)
        worker = Thread(target=validate_url_and_write, args=(q, results))
        worker.setDaemon(True)
        worker.start()
    q.join()
    return results
