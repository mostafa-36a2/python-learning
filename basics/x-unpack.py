def func(a, b, c):
    print(f"a={a}, b={b}, c={c}")


my_list = [1, 2, 3]
func(my_list[0], my_list[1], my_list[2])  # a=1, b=2, c=3
func(*my_list)  # a=1, b=2, c=3

my_dict = {"c": 12, "b": 1, "a": -2}
print(my_dict)  # {'c': 12, 'b': 1, 'a': -2}
print(*my_dict, sep=".")  # c.b.a
func(**my_dict)  # a=-2, b=1, c=12

a = [*"RealPython"]
print(a)  # ['R', 'e', 'a', 'l', 'P', 'y', 't', 'h', 'o', 'n']
print(*a)  # R e a l P y t h o n

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
d3 = {**d1, **d2}
print(d3)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}
