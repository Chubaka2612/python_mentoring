def show_min_max(test_list):
    print("min: " + str(find_min(test_list)))
    print("max: " + str(find_max(test_list)))


def find_min(list):
    test_min = None
    for item in list:
        number = get_int(item)
        if not bool(number):
            continue
        elif not bool(test_min):
            test_min = number
        elif number < test_min:
            test_min = number
    return test_min


def find_max(test_list):
    test_max = None
    for item in test_list:
        number = get_int(item)
        if not bool(number):
            continue
        elif not bool(test_max):
            test_max = number
        elif number > test_max:
            test_max = number
    return test_max


def get_int(item):
    try:
        if item is not None:
            return int(item)
    except ValueError:
        try:
            return int(float(item))
        except ValueError:
            return None
