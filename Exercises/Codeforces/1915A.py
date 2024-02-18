# A. Odd One Out
# https://codeforces.com/contest/1915/problem/A
t = int(input())
for i in range(t):
    a, b, c = list(map(int, input().split()))
    if a == b:
        print(c)
    elif a == c:
        print(b)
    else:
        print(a)
