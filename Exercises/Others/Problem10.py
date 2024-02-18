from collections import Counter


def PrintWordsOccurrenceAdvanced(s):
    dict_of_words = Counter(s.split(" "))
    for word in dict_of_words:
        print(f"[{dict_of_words[word]}] {word}")


PrintWordsOccurrenceAdvanced(
    "I am happy, I am a doctor, I like chocolate, I like ice cream."
)


def PrintWordsOccurrenceNaiive(s):
    words = s.split(" ")
    counter = Counter(words)
    print(counter)

    dict_of_words = {}
    for word in words:
        if word in dict_of_words:
            dict_of_words[word] += 1
        else:
            dict_of_words[word] = 1

    for word in dict_of_words:
        x = dict_of_words[word]
        print(f"[{x}] {word}")
