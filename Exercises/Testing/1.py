length = int(input("enter num : "))

weidth = int(input("enter num : "))

result = int(length * weidth)

if result % 2 == 0 or 1:
    print(result // 42)

else:
    print((result - 1) // 2)
