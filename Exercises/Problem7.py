s = input("Please enter a string: ")
a = input("Please enter one letter:")
a_count = s.count(a)
print("letter count = ", a_count)

next_start = 0
for i in range(a_count):
    letter_index = s.find(a, next_start)
    print(f"'{a}' found at index {letter_index}")
    next_start = letter_index + 1
