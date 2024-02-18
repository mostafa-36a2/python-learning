def decorator(f):
    def b(*args):
        print ("calling "+f.__name__)
        return f(*args)
    return b

@decorator
def func(a, b):
    return a*b

@decorator
def func2(a,b):
    return a+b

func(1,2)
func2(1,3)
