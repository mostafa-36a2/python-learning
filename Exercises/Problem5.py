def DoubleChars(s):
    result = ""
    for c in s:
        result += c + c
    return result


x = DoubleChars("Iron Man")
print(x)
