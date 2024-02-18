t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    l = [0] * len(a)
    index = 1
    while index < len(a):
        if a[index] != a[index - 1]:
            l[index] = index
        else:
            l[index] = l[index - 1]
        index += 1

    for _ in range(q):
        left, right = list(map(int, input().split()))
        if l[left - 1] != l[right - 1]:
            i = l[right - 1]
            j = l[right - 1] + 1
            print(i, j)
        else:
            print(-1, -1)
