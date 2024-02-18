import math

s = [input("Please enter the number of groups: "), input()][1]
c = {4: s.count("4"), 3: s.count("3"), 2: s.count("2"), 1: s.count("1")}
x = math.ceil((c[1] - min(c[3], c[1]) - min(c[1], 2) * (c[2] % 2)) / 4)
print("The minimum taxis required is ", c[4] + c[3] + c[2] // 2 + c[2] % 2 + x)
