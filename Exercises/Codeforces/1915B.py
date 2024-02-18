# https://codeforces.com/contest/1915/problem/B
# B. Not Quite Latin Square
t = int(input())

for _ in range(t):
    l = ""
    l1 = input()
    l2 = input()
    l3 = input()
    if "?" in l1:
        l = l1
    if "?" in l2:
        l = l2
    if "?" in l3:
        l = l3

    for x in ("A", "B", "C"):
        if x not in l:
            print(x)
