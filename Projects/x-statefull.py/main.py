# https://www.geeksforgeeks.org/python-convert-string-dictionary-to-dictionary/
import colorama

phone_book: dict = {}
FILE_NAME = "storage.txt"


def save_my_phone_book(pb):
    file = open(FILE_NAME, "w")
    file.write(str(pb))


def restore_my_phone_book():
    file = open(FILE_NAME, "r")
    s = file.read()
    d = {}
    if s != "":
        try:
            d = eval(s)
        except SyntaxError as e:
            print(f"SyntaxError while reading data, {e}")
            d = {}
    return d


phone_book = restore_my_phone_book()

while True:
    choice = input(
        colorama.Back.GREEN
        + "Choose: 'name' or 'tel' , 'quite': "
        + colorama.Style.RESET_ALL
    )
    if choice == "name":
        name = input(
            colorama.Back.BLUE
            + "Please enter the name to show: "
            + colorama.Style.RESET_ALL
        )
        if name in phone_book:
            print(f"The phone number of {name} is {phone_book[name]}")
        else:
            print(f"There is no phone number for {name}")
    elif choice == "tel":
        name = input(
            colorama.Back.CYAN + "Please enter the name: " + colorama.Style.RESET_ALL
        )
        tel = input(
            colorama.Back.CYAN + "Please enter the tel: " + colorama.Style.RESET_ALL
        )
        phone_book[name] = tel
        save_my_phone_book(phone_book)
    elif choice == "quite":
        print("Goodbye")
        break
    else:
        print("Bad choice")
