from collections import defaultdict


def main(s):
    sections = s.split("W")
    for section in sections:
        # print("Parse section", section)

        if len(section) == 0:
            continue

        if len(section) == 1:
            print("NO")
            return

        R = 0
        B = 0
        for item in section:
            if item == "R":
                R += 1
            else:
                B += 1
        if R == 0 or B == 0:
            print("NO")
            return

    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    # a = list(map(int, input().split()))
    s = input()
    main(s)
