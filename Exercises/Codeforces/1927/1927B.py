debug = False
from collections import defaultdict


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        res = []
        d = defaultdict(list)
        d[0] = list("abcdefghijklmnopqrstuvwxyz")
        for x in a:
            c = d[x].pop()
            res.append(c)
            d[x + 1].append(c)
        print("".join(res))
        # 0 -> new
        # 1 give any of the ones
        # 2 give any of the twos


main()
