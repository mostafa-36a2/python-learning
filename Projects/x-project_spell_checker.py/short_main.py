import Levenshtein as Leve


def nearest(w: str, words):

    distances = [Leve.distance(dw, w.lower()) for dw in words]
    return words[min(range(len(distances)), key=distances.__getitem__)]


with open("dict.txt", "r") as file:
    my_words = [word.lower() for word in file.read().splitlines()]

assert len(my_words) > 0, "No content in dictionary."

print(" ".join([nearest(word.lower(), my_words) for word in input().split(" ")]))
