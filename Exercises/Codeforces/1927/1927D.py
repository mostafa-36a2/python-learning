debug = False
from collections import defaultdict

a = []
d = {}


class Node:

    def __init__(self, l, r, s, left_child, right_child):
        self.l = l
        self.r = r
        self.s = s
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return f"[{self.l} -> {self.r}]: {self.s}"

    def __str__(self):
        return f"[{self.l} -> {self.r}]: {self.s}"


def query_tree(l, r):
    res = 1
    d[(l, r)] = res


from bisect import bisect_left

powers_of_2 = []
for i in range(21):
    powers_of_2.append(2**i)


def get_next_power_of_2(num):
    res = bisect_left(powers_of_2, num)
    return powers_of_2[res]
    # print(powers_of_2[res])


# print(get_next_power_of_2(10))
# print(get_next_power_of_2(20))
# print(get_next_power_of_2(50))
# print(get_next_power_of_2(100))

# exit()

assert get_next_power_of_2(10) == 16
assert get_next_power_of_2(20) == 32
assert get_next_power_of_2(50) == 64
assert get_next_power_of_2(100) == 128


def create_tree(childs):
    len_childs = len(childs)
    node = Node(0, len_childs, None, None, None)
    mid = get_next_power_of_2(len_childs) / 2


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    childs = [
        Node(index, index, set([value]), None, None) for index, value in enumerate(a)
    ]

    tree = create_tree(childs)

    index = 0
    while index < len(childs):
        node = Node.create_node(childs[index], childs[index + 1])

    print(childs)
    q = int(input())
    for _ in range(q):
        l, r = list(map(int, input().split()))
