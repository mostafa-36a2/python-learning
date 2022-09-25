n = int(input())

result = []
for i in range(n):
    s = input()
    team_count = s.count("1")
    if team_count >= 2:
        problem_decision = 1
    else:
        problem_decision = 0

    result.append(problem_decision)

x = sum(result)

print(x)
