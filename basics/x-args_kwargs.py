# https://realpython.com/python-kwargs-and-args/
def function(*args):
    print(args)


def kwfunction(**kwargs):
    print(kwargs)


function(1, 2, 3)
function("Mostafa", "Test", "Hello")
function(1, "Hello", ["x", "y", "z"])

kwfunction(a="A arg", b="B arg")
kwfunction(my_int=12, x=35)
kwfunction(x="doroob", y="inmaa")
