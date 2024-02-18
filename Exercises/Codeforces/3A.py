d = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}

# A. Shortest path of the king
king_place = input()
destination = input()

kx = d[king_place[0]]
ky = int(king_place[1]) - 1

dx = d[destination[0]]
dy = int(destination[1]) - 1
moves = []
while not (kx == dx and ky == dy):
    move = ""
    if kx < dx:
        move += "R"
        kx += 1
    elif dx < kx:
        move += "L"
        kx -= 1

    if ky < dy:
        move += "U"
        ky += 1

    elif dy < ky:
        move += "D"
        ky -= 1

    moves.append(move)

print(len(moves))
if moves:
    for move in moves:
        print(move)
