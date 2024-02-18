def X(d: dict, index1: str, index2: str):  # Should return an object
    class _X(type(d[index1][index2])):
        d: dict
        index1: str
        index2: str

        @classmethod
        def make(cls, d: dict, index1: str, index2: str):
            self = cls(d[index1][index2])  # Call the original constructor
            self.d = d
            self.index1 = index1
            self.index2 = index2
            return self

        @property
        def value(self):
            return self.d[self.index1][self.index2]

        @value.setter
        def value(self, value):
            self.d[self.index1][self.index2] = value

    return _X.make(d, index1, index2)


def a_iterator(a):
    first = X(a, "a", "d")
    second = X(a, "f", "d")
    yield first
    yield second


if __name__ == "__main__":
    a = {"a": {"b": "c", "d": "test"}, "f": {"b": "c", "d": "hi"}}

    c = a_iterator(a)

    # next(c).value = 10
    # next(c).value = 20
    first = next(c)
    second = next(c)
    print(first, second)
    print(a)
    first.value = "changed1"
    second.value = "changed2"
    print(a)
