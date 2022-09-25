n, h = tuple(map(int, input().split()))
ai = list(map(int, input().split()))
print(max([sum(ai[max(0, i - h // 3) : min(n, i + h // 3 + 1)]) for i in range(0, n)]))
