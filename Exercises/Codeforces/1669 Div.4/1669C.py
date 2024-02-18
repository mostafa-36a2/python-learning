from collections import defaultdict


def main(a):
    # Odd indeces
    last_odd_index_value = a[0]
    for index in range(0, len(a), 2):
        if last_odd_index_value % 2 != a[index] % 2:
            print("NO")
            return
        else:
            last_odd_index_value = a[index]

    last_even_index_value = a[1]
    for index in range(1, len(a), 2):
        if last_even_index_value % 2 != a[index] % 2:
            print("NO")
            return
        else:
            last_even_index_value = a[index]

    print("YES")


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    #  Add 1 to every element with an odd index. (Starting from 1)
    # Add 1 to every element with an even index.
    # dermine if after any number of operations it is
    #       possible to make the final array contain only even numbers or only odd numbers.

    main(a)
