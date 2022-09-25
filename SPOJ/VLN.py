n, h = tuple(map(int, input().split()))
# n, h = 5, 3
h = h // 3  # Index distance
ai = list(map(int, input().split()))
# ai = [1, 2, 2, 2, 1]


def collect_from_i(i, n, h, ai):
    current_collect = 0
    for x in range(max(0, i - h), min(n, i + h + 1)):
        # print("Collecting index: ", x)
        current_collect += ai[x]
    return current_collect


max_collect = 0
for i in range(0, n):  # From next index to the end
    # print("Testing index: ", i)
    current_collect = collect_from_i(i, n, h, ai)
    max_collect = max(max_collect, current_collect)
    # print(i, current_collect, max_collect)

print(max_collect)
