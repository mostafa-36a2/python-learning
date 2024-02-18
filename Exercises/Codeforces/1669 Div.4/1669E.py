from collections import defaultdict


def main(a):
    return


def generate_pairs():
    d = {}
    for first in "abcdefghijk":
        for second in "abcdefghijk":
            pair = f"{first}{second}"
            # Others with first:
            possible_peer_second = list("abcdefghijk")
            possible_peer_second.remove(second)
            peers = [f"{first}{other}" for other in possible_peer_second]

            possible_peer_first = list("abcdefghijk")
            possible_peer_first.remove(first)
            more_peers = [f"{other}{second}" for other in possible_peer_first]
            d[pair] = set(peers + more_peers)
    return d


d = generate_pairs()

t = int(input())
for _ in range(t):
    n = int(input())
    # a = list(map(int, input().split()))
    result = 0
    s_count = defaultdict(int)
    for _ in range(n):
        s = input()
        # print(f"Searching {s} in {d[s]}")
        for valid_peer in d[s]:
            if s_count[valid_peer]:
                # print(f"Increase result by {s_count[valid_peer]}")
                result += s_count[valid_peer]
        s_count[s] += 1
    print(result)
    # main(a)
