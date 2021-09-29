def get_multiple_of(limit, divs):
    result = []
    for i in range(1, limit):
        if any(i % div == 0 for div in divs):
            result.append(i)
    return result


def show_sum_multiple_of(limit=10000, divs=(3, 5)):
    print("Total sum for numbers in range 1,", limit, "multiple to", divs, "is", sum(get_multiple_of(limit, divs)))
