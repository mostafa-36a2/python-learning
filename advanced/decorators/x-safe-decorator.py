def safe_guard(default_value=None):
    def safe_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                print(
                    f"""calling [{func.__name__}] with parameters ({args},{kwargs}) raised an exception [{e.__class__.__name__}:{e}]."""
                )
                res = default_value
            else:
                print(f"Calling [{func.__name__}] with no exception.")
            finally:
                return res

        return wrapper

    return safe_decorator


@safe_guard([2, 4, 5])
def my_functino2(a, b, d):
    raise ValueError(a, b, d)


res = my_functino2(1, 2, 3)
print("my_functino2 returned: ", res)
