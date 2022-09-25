import inspect


class LineNo:
    def __str__(self):
        return str(inspect.currentframe().f_back.f_lineno)


__line__ = LineNo()

print(__line__)
print(__line__)
print(__line__)
print(__line__)
