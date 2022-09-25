# https://www.pythonpool.com/python-getch-library/
from getch import getch


def get_clean_input(list_of_allowed_characters):
    a = getch()
    result = ""
    while a != "\n":
        if a in list_of_allowed_characters:
            # https://stackoverflow.com/questions/62532678/getch-takes-input-before-printing
            print(a, end="", flush=True)
            result += a
        else:
            # print("x", end="", flush=True)
            pass
        a = getch()
    print()
    return result


s = get_clean_input(["1", "0"])
print(s)

s = get_clean_input(["a", "b", "c"])
print(s)
