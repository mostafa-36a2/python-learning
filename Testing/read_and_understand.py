lst = []
n = int(input())
for i in range(0, n):
    ele = input()
    lst.append(ele)
for i in range(0, n - 1):
    if lst[i][-1] == lst[i + 1][0]:
        print("Ordering is possible")
        break
    else:
        print("The door cannot be opened.")
        break
