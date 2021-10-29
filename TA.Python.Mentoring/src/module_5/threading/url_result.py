import json


class UrlResult:

    def __init__(self, url, is_ok, status_code):
        self.url = url
        self.is_ok = is_ok
        self.status_code = status_code

    def __str__(self):
        return f"url: {self.url} is_ok: {self.is_ok} status_code: {self.status_code}"


class UrlResultEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UrlResult):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)
