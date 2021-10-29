"""
These are different solutions of "Task 5: Multiples of 3 and 5. Find the best algorithm"

Let's find out which of the proposed algorithms is the most effective
"""

from multiprocessing import Process
from timer import Timer
from module_5.log_configurator import get_logger
log = get_logger('multiples_of_three_and_five')

N = 300000000


def simple_iteration():
    t = Timer()
    res = 0
    t.start()

    for i in range(N):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    log.info("simple_iteration() ->")
    t.stop()
    return res


def several_for_loops():
    t = Timer()
    res = 0
    t.start()

    for i in range(3, N, 3):
        res += i
    for i in range(5, N, 5):
        res += i
    for i in range(15, N, 15):
        res -= i
    log.info("several_for_loops() ->")
    t.stop()
    return res


def iterate_over_fifteen():
    t = Timer()
    range_diff = [0, 3, 5, 6, 9, 10, 12]
    res = 0
    t.start()
    for i in range(0, N, 15):
        for d in range_diff:
            v = i + d
            if v >= N:
                break
            res += v
    log.info("iterate_over_fifteen() ->")
    t.stop()
    return res


def math_formula():
    t = Timer()
    upper = N - 1
    threes = int(3 * (upper / 3) * ((upper / 3) + 1) / 2)
    fives = int(5 * (upper / 5) * ((upper / 5) + 1) / 2)
    fifteens = int(15 * (upper / 15) * ((upper / 15) + 1) / 2)
    t.start()

    res = threes + fives - fifteens
    log.info("math_formula() ->")
    t.stop()
    return res


def run_all_calculations_in_parallel():
    # Use multiprocessing library to run all above functions in parallel
    # Print execution time of each function
    runInParallel(math_formula, iterate_over_fifteen,several_for_loops, simple_iteration)


def runInParallel(*fns):
    proc = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


if __name__ == '__main__':
    run_all_calculations_in_parallel()

