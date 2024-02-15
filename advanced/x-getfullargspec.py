# https://www.geeksforgeeks.org/function-annotations-python/
# https://peps.python.org/pep-3107/
# Python program to illustrate Function Annotations
import inspect


def fib(n:'int'=10, output:'list'=[1,2],*arg,**kwargs)-> 'list[int]':
    return []

print(inspect.getfullargspec(fib))
