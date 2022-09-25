list_of_ec = ["'", "\\", "\n", "\r", "\t", "\b", "\f"]


def CountNoneEscapeCharacters(s):
    total_len = len(s)
    for ec in list_of_ec:
        total_len -= s.count(ec)
    return total_len


x = CountNoneEscapeCharacters("Hello\n\n\n\n\n\t\t\t\t\t\b\b\b\b\b\\\\\\\\'")
print(x)
