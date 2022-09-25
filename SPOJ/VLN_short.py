n, h = tuple(map(int, input().split()))
h = h // 3  # Index distance
ai = list(map(int, input().split()))
max_collect = 0

for i in range(0, n):  # From next index to the end
    current_collect = 0
    for x in range(max(0, i - h), min(n, i + h + 1)):
        current_collect += ai[x]
    max_collect = max(max_collect, current_collect)

print(max_collect)
