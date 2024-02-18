# A. Kalevitch and Chess
# https://codeforces.com/problemset/problem/7/A

res = 0
cols = set()
for i in range(8):
    row = input()
    if "W" not in row:
        # The whole row is painted
        res += 1
        continue

    for i, c in enumerate(row):
        if c == "B":
            if i not in cols:
                cols.add(i)
                res += 1
print(res)
