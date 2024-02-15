import lib
from lib import list_of_numbers

print(lib.list_of_numbers, id(lib.list_of_numbers))
print(list_of_numbers, id(list_of_numbers))

lib.list_of_numbers = [9, 8, 7]

print(lib.list_of_numbers, id(lib.list_of_numbers))
print(list_of_numbers, id(list_of_numbers))
