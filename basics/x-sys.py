def fun1(x):
    print(x)


def fun2(x):
    print(x * x)


class MyClass:
    def func(x):
        print()


r = globals()
r["fun1"](14)
