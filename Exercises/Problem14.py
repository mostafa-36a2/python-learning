n = int(input("Please enter the number of lines: "))

for i in range(n):
    s: str = input()
    if len(s) < 10:
        print(s)
    else:
        print(s[0], len(s) - 2, s[-1], sep="")
