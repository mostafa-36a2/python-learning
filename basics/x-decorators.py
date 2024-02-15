# https://www.geeksforgeeks.org/decorators-in-python/

# defining a decorator
def hello_decorator(func):
    def inner1():
        print("<<<<")
        func()  # calling the actual function now, inside the wrapper function.
        print(">>>>")

    return inner1


@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")


# Same as: function_to_be_used = hello_decorator(function_to_be_used)


function_to_be_used()
