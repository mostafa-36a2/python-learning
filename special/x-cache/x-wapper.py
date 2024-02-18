import time


def memoize(function):
    memo = {}
    print("First time memoize")

    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv = function(*args)
            memo[args] = rv
            return rv

    return wrapper


import inspect


def time_it(function):
    def wrapper(*args, **kwargs):
        start = time.perf_counter_ns()
        res = function(*args, **kwargs)
        end = time.perf_counter_ns()
        this_function_name = inspect.currentframe().f_code.co_name
        print(
            f"function {__name__} + {function.__qualname__} <<{this_function_name}>> takes ",
            end - start,
            " ns",
        )
        return res

    return wrapper


@time_it
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def test(n):
    start = time.perf_counter_ns()
    fibonacci(n)
    end = time.perf_counter_ns()
    print(end - start, " ns")


test(100)
test(100)
test(100)
test(100)
test(100)
