# A. Triangle
# https://codeforces.com/problemset/problem/6/A
n = list(map(int, input().split()))


def is_triangle(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)


def is_segment(a, b, c):
    return a + b == c or a + c == b or b + c == a


def main():
    r = "IMPOSSIBLE"
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            for k in range(j + 1, len(n)):
                if is_triangle(n[i], n[j], n[k]):
                    print("TRIANGLE")
                    return False

                if is_segment(n[i], n[j], n[k]):
                    r = "SEGMENT"
    print(r)


main()
