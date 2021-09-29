def get_int(item):
    try:
        if item is not None:
            return int(item)
    except ValueError:
        try:
            return int(float(item))
        except ValueError:
            return


def get_int_list_via_for(test_list):
    result_list = []
    for item in test_list:
        number = get_int(item)
        if not bool(number):
            continue
        else:
            result_list.append(number)
    return result_list


def get_int_list_via_comprehensions(test_list):
    return [int_item for int_item in (get_int(item) for item in test_list) if int_item]


def get_int_list_via_lambda(test_list):
    return list(filter(lambda x: get_int(x), test_list))
