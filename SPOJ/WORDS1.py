t = int(input())  # 500
for tt in range(t):
    n = int(input())  # 100_000
    list_of_words = []
    for nn in range(n):
        word = input()
        list_of_words.append(word[0] + word[-1])
    print(list_of_words)
