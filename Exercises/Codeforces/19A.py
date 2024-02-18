# the final tournament features n teams (n is always even)
# the first n / 2 teams (according to the standings) come through to the knockout stage
# the standings are made on the following principle:
# for a victory a team gets 3 points,
# for a draw — 1 point,
# for a defeat — 0 points.
# In the first place, teams are ordered in the standings in decreasing order of their points;
#       in the second place — in decreasing order of the difference between scored and missed goals;
#       in the third place — in the decreasing order of scored goals
# it's written in Berland's Constitution that the previous regulation
#       helps to order the teams without ambiguity.

# You are asked to write a program that,
#       by the given list of the competing teams
#       and the results of all the matches,
#       will find the list of teams that managed to get through to the knockout stage.

n = int(input())  # amount of the teams

teams = []
for _ in range(n):
    teams.append(input())  # lowed and upper latin letters
    # len<30

from collections import defaultdict

points = defaultdict(int)
missed_goals = defaultdict(int)
goals = defaultdict(int)
for _ in range(int((n * (n - 1)) // 2)):
    teams, result = input().split(" ")
    t1, t2 = teams.split("-")
    r, ll = list(map(int, result.split(":")))  # (0 ≤ num1, num2 ≤ 100

    if r == ll:  # draw
        points[t1] += 1
        points[t2] += 1
    elif r > ll:
        points[t1] += 3
        points[t2] += 0
    elif r < ll:
        points[t2] += 3
        points[t1] += 0

    missed_goals[t1] += ll
    missed_goals[t2] += r

    goals[t1] += r
    goals[t2] += ll

final_result = {}

for team in points:
    final_result[team] = (points[team], goals[team] - missed_goals[team], goals[team])

d = {
    k: v
    for k, v in sorted(final_result.items(), key=lambda item: item[1], reverse=True)
}
print(d)
p = list(d.keys())
p = sorted(p[: len(p) // 2])
print("\n".join(p))
# 4
# TeMnHVvWKpwlpubwyhzqvc
# AWJwc
# bhbxErlydiwtoxy
# EVASMeLpfqwjkke
# AWJwc-TeMnHVvWKpwlpubwyhzqvc 37:34
# bhbxErlydiwtoxy-TeMnHVvWKpwlpubwyhzqvc 38:99
# bhbxErlydiwtoxy-AWJwc 33:84
# EVASMeLpfqwjkke-TeMnHVvWKpwlpubwyhzqvc 79:34
# EVASMeLpfqwjkke-AWJwc 24:37
# EVASMeLpfqwjkke-bhbxErlydiwtoxy 3:6
