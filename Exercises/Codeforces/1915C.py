# C. Can I Square?
# https://codeforces.com/contest/1915/problem/C
import math

t = int(input())
for _ in range(t):
    n = int(input())
    # Number of squares in each bucket
    a = list(map(int, input().split()))
    s = sum(a)
    ss = math.sqrt(s)
    if int(ss) == ss:
        print("YES")
    else:
        print("NO")
    # Each square is of 1x1 sides
