from collections import defaultdict


def main(a):
    return


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = 0
    s_count = defaultdict(int)
    #  The i-th candy has weight wi.
    # Alice can eat any number of candies from the left
    # Bob can eat any number of candies from the right
    left_pointer = 0
    right_pointer = len(a) - 1

    alice = 0
    bob = 0
    max_till_now = 0
    count = 0
    while left_pointer <= right_pointer:
        # print(f"Alice ate {a[left_pointer]}")
        count += 1
        alice += a[left_pointer]
        left_pointer += 1
        while alice > bob and left_pointer <= right_pointer:
            # print(f"Bob ate {a[right_pointer]}")
            count += 1
            bob += a[right_pointer]
            right_pointer -= 1

        # print(f"Now alice({alice}) and bob({bob})")
        if alice == bob:
            max_till_now = count
    print(max_till_now)
