from threading import Thread

import requests

from status_code import Status
from url_result import UrlResult


def validate_url_and_write(url, result, index):
    try:
        status = requests.get(url).status_code
        is_ok = status == Status.OK
        url_result = UrlResult(url, is_ok, status)
    except:
        url_result = UrlResult(url, False, None)
    print("Processing:" + str(url_result))
    result[index] = url_result


def validate_urls(urls):
    results = [{} for _ in urls]
    threads = []
    for i in range(len(urls)):
        process = Thread(target=validate_url_and_write, args=[urls[i], results, i])
        process.start()
        threads.append(process)
    for process in threads:
        process.join()
    return results