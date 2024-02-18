import math

n, k = list(map(int, input().split()))
if k == 0:
    print("YES")
elif k > 250:
    print("NO")
else:
    numbers = [1] * 1001
    numbers[0] = 0
    numbers[1] = 0
    primes = []
    for i in range(2, int(1 + math.sqrt(1000))):
        for j in range(i * 2, 1000, i):
            numbers[j] = 0

    for i in range(len(numbers)):
        if numbers[i]:
            primes.append(i)

    sum_np_1 = set()

    for i in range(len(primes) - 1):
        sum_np_1.add(primes[i] + primes[i + 1] + 1)

    for i in range(2, n + 1):
        if numbers[i]:
            if i in sum_np_1:
                k -= 1
                if k == 0:
                    print("YES")
                    break
    else:
        print("NO")
