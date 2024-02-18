x1, y1, x2, y2, x3, y3 = list(map(int, input().split()))  # |x|< 100


def d_sq(x11, x22, y11, y22):
    return abs(x22 - x11) ** 2 + abs(y22 - y11) ** 2


a, b, c, d, e, f = (0, 0, 0, 0, 0, 0)
d1 = d_sq(x1 + a, x2 + b, y1 + c, y2 + d)
d2 = d_sq(x2 + b, x3 + e, y2 + d, y3 + f)
d3 = d_sq(x3 + e, x1 + a, y3 + f, y1 + d)

d1, d2, d3 = sorted([d1, d2, d3])

if d1**2 + d2**2 == d3**2:
    print("RIGHT")
    exit(0)

for i in (1, -1):
    a, b, c, d, e, f = (i, 0, 0, 0, 0, 0)
    d1 = d_sq(x1 + a, x2 + b, y1 + c, y2 + d)
    d2 = d_sq(x2 + b, x3 + e, y2 + d, y3 + f)
    d3 = d_sq(x3 + e, x1 + a, y3 + f, y1 + d)

    d1, d2, d3 = sorted([d1, d2, d3])

    if d1**2 + d2**2 == d3**2:
        print("ALMOST")
        exit(0)

for i in (1, -1):
    a, b, c, d, e, f = (0, i, 0, 0, 0, 0)
    d1 = d_sq(x1 + a, x2 + b, y1 + c, y2 + d)
    d2 = d_sq(x2 + b, x3 + e, y2 + d, y3 + f)
    d3 = d_sq(x3 + e, x1 + a, y3 + f, y1 + d)

    d1, d2, d3 = sorted([d1, d2, d3])

    if d1**2 + d2**2 == d3**2:
        print("ALMOST")
        exit(0)

for i in (1, -1):
    a, b, c, d, e, f = (0, 0, i, 0, 0, 0)
    d1 = d_sq(x1 + a, x2 + b, y1 + c, y2 + d)
    d2 = d_sq(x2 + b, x3 + e, y2 + d, y3 + f)
    d3 = d_sq(x3 + e, x1 + a, y3 + f, y1 + d)

    d1, d2, d3 = sorted([d1, d2, d3])

    if d1**2 + d2**2 == d3**2:
        print("ALMOST")
        exit(0)

for i in (1, -1):
    a, b, c, d, e, f = (0, 0, 0, i, 0, 0)
    d1 = d_sq(x1 + a, x2 + b, y1 + c, y2 + d)
    d2 = d_sq(x2 + b, x3 + e, y2 + d, y3 + f)
    d3 = d_sq(x3 + e, x1 + a, y3 + f, y1 + d)

    d1, d2, d3 = sorted([d1, d2, d3])

    if d1**2 + d2**2 == d3**2:
        print("ALMOST")
        exit(0)

for i in (1, -1):
    a, b, c, d, e, f = (0, 0, 0, 0, i, 0)
    d1 = d_sq(x1 + a, x2 + b, y1 + c, y2 + d)
    d2 = d_sq(x2 + b, x3 + e, y2 + d, y3 + f)
    d3 = d_sq(x3 + e, x1 + a, y3 + f, y1 + d)

    d1, d2, d3 = sorted([d1, d2, d3])

    if d1**2 + d2**2 == d3**2:
        print("ALMOST")
        exit(0)


for i in (1, -1):
    a, b, c, d, e, f = (0, 0, 0, 0, 0, i)
    d1 = d_sq(x1 + a, x2 + b, y1 + c, y2 + d)
    d2 = d_sq(x2 + b, x3 + e, y2 + d, y3 + f)
    d3 = d_sq(x3 + e, x1 + a, y3 + f, y1 + d)

    d1, d2, d3 = sorted([d1, d2, d3])

    if d1**2 + d2**2 == d3**2:
        print("ALMOST")
        exit(0)

print("NEITHER")
