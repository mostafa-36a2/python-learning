import time
from functools import lru_cache


@lru_cache
def calculate_thing():
    a = 0
    for i in range(1000000):
        a += i
    return a


def test():
    start = time.perf_counter_ns()
    calculate_thing()
    end = time.perf_counter_ns()
    print(end - start, " ns")


test()
test()
test()
test()
test()
test()
test()
