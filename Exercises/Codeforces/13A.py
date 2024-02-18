A = int(input())


def numberToBase(n, b):
    if n == 0:
        return [0]

    res = []
    while n > 0:
        res.append(n % b)
        n //= b

    res.reverse()
    return res


res = 0
for base in range(2, A):
    x = A
    cc = numberToBase(x, base)
    res += sum(cc)
nom = res
denom = A - 2
for i in range(denom, 1, -1):
    while nom % i == 0 and denom % i == 0:
        nom //= i
        denom //= i

print(f"{nom}/{denom}")
