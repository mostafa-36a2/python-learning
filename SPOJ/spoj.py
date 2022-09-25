n = int(input("Please enter the positive integer N:"))
if n < 1:
    print("N must be greater than 0!")
else:
    print(f"The number-triangle that has {n} lines is:")
    for i in range(n):
        line = ""
        for j in range(i + 1):
            if line:
                line += " "
            line += str(j + 1)
        print(line)

exit()
print("Please enter numerator: ")
print("Please enter denominator: ")
while True:
    i = input()
    if i != "":
        numerator = int(i)
        break
while True:
    i = input()
    if i != "":
        denominator = int(i)
        break

if denominator == 0:
    print("The denominator can’t be zero!")
else:
    res = numerator / denominator
    print(f"Result: {numerator} / {denominator} = {res:.6f}")


exit()
# your code goes here
from math import sqrt

num = input("Please enter any number: ")
num = float(num)
if num < 0:
    print("Accept positive number only!")
else:
    num_sqrt = sqrt(num)
    print(f"Square root of {num:.6f} is {num_sqrt:.6f}")

exit()
# Enter Numiric array, with N element
# Display minimum number
num = int(input("How many element of numeric array:"))
a = []
for i in range(1, num + 1):
    x = int(input(f"The value of a[{i}] is:"))
    print(x)
    a.append(x)
print("Min:" + str(min(a)))
