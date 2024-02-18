def main():
    t = int(input())

    for _ in range(t):
        n, m = list(map(int, input().split()))
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        max_pone = sum(a)
        max_ptwo = sum(b)
        res = ""
        if max_pone > m:
            player_one_win = "Y"
        else:
            player_one_win = "N"

        if max_ptwo > n:
            player_two_win = "Y"
        else:
            player_two_win = "N"

        if player_one_win == "Y" and player_two_win == "Y":
            draw = "Y"
        else:
            draw = "N"

        print(f"{player_one_win}{draw}{player_two_win}")


main()
