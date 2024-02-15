debug = False
from collections import defaultdict


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input()
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] == "W":
                l += 1
            if s[r] == "W":
                r -= 1
            if s[l] == "B" and s[r] == "B":
                print(r - l + 1)
                break
        else:
            if s[l] == "B":
                print(1)
            else:
                print(0)


main()
