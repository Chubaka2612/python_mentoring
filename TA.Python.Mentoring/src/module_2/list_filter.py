def get_int(item):
    try:
        return int(float(item))
    except (TypeError, ValueError):
        return


def get_int_list_via_for(test_list):
    result_list = []
    for item in test_list:
        number = get_int(item)
        result_list.append(number) if number or number == 0 else None
    return result_list


def get_int_list_via_comprehensions(test_list):
    return [int_item for int_item in (get_int(item) for item in test_list) if int_item or int_item == 0]


def get_int_list_via_lambda(test_list):
    return list(filter(lambda x: get_int(x), test_list))
