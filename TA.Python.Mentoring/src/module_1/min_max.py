def show_min_max(test_list):
    print("min:", min(get_int_list(test_list)))
    print("max:", max(get_int_list(test_list)))


def get_int_list(test_list):
    result_list = []
    for item in test_list:
        number = get_int(item)
        if not bool(number):
            continue
        else:
            result_list.append(number)
    return result_list


def get_int(item):
    try:
        if item is not None:
            return int(item)
    except ValueError:
        try:
            return int(float(item))
        except ValueError:
            return None
