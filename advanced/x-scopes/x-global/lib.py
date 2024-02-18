def init_lib():
    def func1():
        global x
        x=1
    return func1

func = init_lib()
func()

print(x)