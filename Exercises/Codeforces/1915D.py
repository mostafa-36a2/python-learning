# D. Unnatural Language Processing
# https://codeforces.com/contest/1915/problem/D
t = int(input())
for _ in range(t):
    len_ = int(input())
    letters = input()
    res = []
    i = len(letters) - 1
    while i >= 0:
        # Is V
        # Possibilities are only: CV
        if letters[i] in "ae":
            res.append(letters[i])
            res.append(letters[i - 1])
            res.append(".")
            i -= 2
        else:
            res.append(letters[i])
            res.append(letters[i - 1])
            res.append(letters[i - 2])
            res.append(".")
            i -= 3
    res.reverse()
    print("".join(res[1:]))
