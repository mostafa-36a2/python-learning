from collections import defaultdict


def main():
    n = int(input())
    d = defaultdict(int)
    final_scores = defaultdict(list)
    max_final_score = -99999
    accu_scores = list()

    for _ in range(n):
        name, score = input().split(" ")
        # Running score
        d[name] += int(score)

        # Accumulation results
        accu_scores.append((name, d[name]))

    for name, score in d.items():
        max_final_score = max(max_final_score, score)
        final_scores[score].append(name)

    for name, acc_score in accu_scores:
        if name in final_scores[max_final_score] and acc_score >= max_final_score:
            print(name)
            return False


main()
