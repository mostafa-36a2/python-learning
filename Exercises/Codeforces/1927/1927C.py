debug = False


def main():
    t = int(input())
    for _ in range(t):
        n, m, k = list(map(int, input().split()))
        ma = map(int, input().split())
        mb = map(int, input().split())
        a = set()
        for c in ma:
            if c <= k:
                a.add(c)
        if debug:
            print(f"a set: {a}")
        b = set()
        # b contains only numbers not in a
        for c in mb:
            if c <= k:
                b.add(c)
        if debug:
            print(f"b set: {b}")

        both_a_and_b = a.union(b)
        if debug:
            print(f"both_a_and_b set: {both_a_and_b}")

        if len(both_a_and_b) < k or len(b) < int(k / 2) or len(a) < int(k / 2):
            print("NO")
            continue

        in_a_not_in_b = a - b  # must get
        if debug:
            print(f"in_a_not_in_b set: {in_a_not_in_b}")
        if len(in_a_not_in_b) > k / 2:
            print("NO")
            continue

        in_b_not_in_a = b - a  # must get
        if debug:
            print(f"in_b_not_in_a set: {in_b_not_in_a}")
        if len(in_b_not_in_a) > k / 2:
            print("NO")
            continue

        # https://www.w3schools.com/python/ref_set_intersection.asp
        in_a_and_in_b = a.intersection(b)
        if debug:
            print(f"in_a_and_in_b set: {in_a_and_in_b}")
        tobe_got_from_a = int(k / 2) - len(in_a_not_in_b)
        if debug:
            print(f"tobe_got_from_a:{tobe_got_from_a}")
        tobe_got_from_b = int(k / 2) - len(in_b_not_in_a)
        if debug:
            print(f"tobe_got_from_b:{tobe_got_from_b}")
        if len(in_a_and_in_b) == tobe_got_from_a + tobe_got_from_b:
            print("YES")
        else:
            print("NO")


main()
