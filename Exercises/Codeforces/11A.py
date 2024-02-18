import math

n, d = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0
for i in range(1, len(b)):
    if b[i - 1] < b[i]:
        continue
    else:
        times = math.ceil((b[i - 1] - b[i] + 1) / d)
        b[i] += times * d
        res += times
        # print(i, times)
print(res)
