# 1- Normal function
def func(a, b):
    res = int(a) + int(b)
    print(res)
    return res


res = func(1, 0)

res = func("1", "1")

# 2- Normal try-except
try:
    res = func("1", "2a")
except Exception as e:
    print(f"calling func raised an exception {e}, with parameters '1', '2a' ")
    res = None


# 3- decorator for try-except
def safe_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as e:
            print(
                f"calling [{func.__name__}] raised a [{e.__class__.__name__}] exception {e}, with parameters ({args},{kwargs}) "
            )
            res = None
        return res

    return wrapper


@safe_decorator
def my_function(a, b, c):
    raise ValueError(a, b, c)


my_function(1, 2, 3)


# 4- decorator of decorator for try-except, and adding value to be retuend on exceptin
def safe_guard(default_value=None):
    def safe_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                print(
                    f"calling [{func.__name__}] raised a [{e.__class__.__name__}] exception {e}, with parameters ({args},{kwargs}) "
                )
                res = default_value
            return res

        return wrapper

    return safe_decorator


@safe_guard([2, 4, 5])
def my_functino2(a, b, d):
    raise ValueError(a, b, d)


res = my_functino2(1, 2, 3)
print(res)
