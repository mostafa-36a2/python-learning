from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)

    for i in a:
        d[i] += 1
        if d[i] >= 3:
            print(i)
            break
    else:
        print(-1)
