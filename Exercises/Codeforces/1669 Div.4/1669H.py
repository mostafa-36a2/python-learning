from collections import defaultdict

t = int(input())
for _ in range(t):
    n, k = list(map(int, input().split()))
    # You can perform at most k operations
    # you can choose an index i (1≤i≤n) and set the j-th bit of ai to 1
    a = list(map(int, input().split()))

    result = 0
    for mask_power in range(30, -1, -1):
        mask = 2**mask_power
        count = 0
        for num in a:
            if num & mask == 0:
                count += 1
        if count == 0:
            result += mask
        elif count <= k:
            k -= count
            result += mask
        else:
            # Not possible to use this value
            pass
    print(result)
