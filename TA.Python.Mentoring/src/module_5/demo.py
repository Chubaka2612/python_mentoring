
import file_helper
from module_5 import url_validator


def main():
    urls = file_helper.read_file()
    res = url_validator.validate_urls(urls)
    file_helper.write_to_json_file(res)

main()
