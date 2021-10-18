import list_filter
import ip_validator
import file_data_transformer
import find_util
import list_directory_util

def main():
    print("==========task#1")
    print("==========task#1.1 get int list via for loop")
    assert list_filter.get_int_list_via_for([1, 2, 'a', 'b']) == [1, 2]

    print("==========task#1.2 get int list via list comprehensions")
    assert list_filter.get_int_list_via_comprehensions([1, 2, 'a', 'b', 1.3]) == [1, 2, 1]

    print("==========task#1.3 get int list via lambda")
    assert list_filter.get_int_list_via_lambda([1, 2, 'a', 'b']) == [1, 2]

    print("==========task#2")
    print("==========task#2.1 validate ip address via regex")
    assert ip_validator.is_ip_valid("192.168.0.1")
    assert not ip_validator.is_ip_valid("700")
    assert not ip_validator.is_ip_valid("")
    assert ip_validator.is_ip_valid("0.0.0.1")
    assert not ip_validator.is_ip_valid("10.100.500.32")

    print("==========task#2.2 validate ip address via socket lib")
    assert ip_validator.is_ip_valid_via_socket("192.168.0.1")
    assert not ip_validator.is_ip_valid_via_socket("700")
    assert not ip_validator.is_ip_valid_via_socket("")
    assert ip_validator.is_ip_valid_via_socket("0.0.0.1")
    assert not ip_validator.is_ip_valid_via_socket("10.100.500.32")

    print("==========task#3 csv json file rw")
    data = file_data_transformer.read_csv_file('resources/cars.csv')
    file_data_transformer.write_to_json_file('resources/cars.json', data)

    print("==========task#4 find file or directory util")
    print(find_util.find('C:\\WORK\\Projects\\Python\\TA.Python.Mentoring\\module_2\\', '*.json', 'f'))
    print(find_util.find('C:\\WORK\\Projects\\Python\\TA.Python.Mentoring\\module_2\\', 'res*', 'd'))

    print("==========task#5 directory list util")
    print(list_directory_util.list_directory_files('C:\\WORK\\Projects\\Python\\TA.Python.Mentoring\\module_2\\'))


main()
