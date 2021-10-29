import json
from url_result import UrlResultEncoder


def read_file(file_name='../resources/links.txt'):
    content = [line.strip() for line in open(file_name, 'r')]
    return content


def write_to_json_file(data, filename='../resources/data.json'):
    with open(filename, "w") as write_file:
        json.dump(data, write_file, indent=4, cls=UrlResultEncoder)
