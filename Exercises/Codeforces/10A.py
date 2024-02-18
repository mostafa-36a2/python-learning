n, P1, P2, P3, T1, T2 = list(map(int, input().split()))

last_r = 0
res = 0
for _ in range(n):
    l, r = list(map(int, input().split()))

    res += (r - l) * P1 + int(last_r > 0) * (
        min(l - last_r, T1) * P1
        + min(max(l - last_r - T1, 0), T2) * P2
        + max(l - last_r - T1 - T2, 0) * P3
    )
    last_r = r

# 6 88 28 100 53 36
# 440 445
# 525 614
# 644 844
# 1238 1261
# 1305 1307
# 1425 1434
# 85540
print(res)
