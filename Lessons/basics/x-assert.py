a = 2
b = 3
assert a + b == 5, "2 + 3 should be equal to 5, not " + str(a + b)
print(f"a+b={a+b}")


class fake_number:
    x: int

    def __init__(self, __x):
        self.x = __x

    def __add__(self, other):
        return self.x * other.x


c = fake_number(2)
d = fake_number(3)
assert c + d == 6, "c(2) + d(3) should be equal to 5, not " + str(c + d)

e = "2"
f = "3"
assert e + f == 5, "e(2) + f(3) should be equal to 5, not " + str(e + f)
