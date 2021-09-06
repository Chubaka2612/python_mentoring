def show_fizz_buzz(end_range=100, fizz_mod=3, buzz_mod=5):
    try:
        range_num = int(end_range)
        if range_num < 0:
            raise Exception("End of range should be positive")
    except ValueError:
        print("Input end of range should have number type")
    except Exception as e:
        print(e)
    for i in range(1, range_num):
        result = ""
        if i % fizz_mod == 0:
            result += "Fizz"
        if i % buzz_mod == 0:
            result += "Buzz"
        if not bool(result):
            result = i
        print(result)
