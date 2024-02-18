from collections import defaultdict


def print_grid(rows):
    for row in rows:
        print("".join(row))


def move_tick(rows):
    number_of_changes = 0
    # Start from below, no need for the last line
    for yindex in range(len(rows) - 2, -1, -1):
        row = rows[yindex]
        for xindex, cell in enumerate(row):
            # stone
            if cell == "*" and rows[yindex + 1][xindex] == ".":
                rows[yindex + 1][xindex] = "*"
                rows[yindex][xindex] = "."
                number_of_changes += 1

    return number_of_changes != 0


t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    rows = []
    for _ in range(n):
        rows.append(list(input()))

    keep_going = True
    while keep_going:
        keep_going = move_tick(rows)

    print_grid(rows)
    print()
