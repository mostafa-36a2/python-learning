# - User input
# - In dictionary (Case insensitive)
# - Find the nearest word from dictionary
# - Output For the corrected sentece

import Levenshtein


# FUNCTION
def check_dict(words_list):
    word: str
    for word in words_list:
        if word != word.lower():
            return False
    return True


# ASSERTIONS TO CHECK THAT THE FUNCTION IS GOOD
assert check_dict(["he", "she", "it"])
assert not check_dict(["he", "she", "MOSTAFA"])
assert not check_dict(["bbbbbbB", "aaAaaaa", "mostaaaaa"])


def init_dict():
    with open("dict.txt", "r") as file:
        content = file.read()
    list_of_content = content.splitlines()

    # new_list = []
    # for word in list_of_content:
    #    new_list.append(word.lower())

    return [word.lower() for word in list_of_content]


# My dictionary
my_words = init_dict()

# All words must be in lower cases
if not check_dict(my_words):
    print("Dictionary is not all in lower cases.")
    exit(1)


def ascii_sum(word):
    sum = 0
    for c in word:
        sum += ord(c) - 96
    return sum


assert ascii_sum("") == 0
assert ascii_sum("a") == 1
assert ascii_sum("ab") == 1 + 2


def common_letters(word1, word2):
    counter = 0
    for c in word1:
        if c in word2:
            counter += 1
            word1 = word1.replace(c, "", 1)
            word2 = word2.replace(c, "", 1)
    return counter


assert common_letters("hello", "hello") == 5
assert common_letters("i am", "i a") == 3
assert common_letters("eeeee", "ee") == 2
assert common_letters("abcdefg", "ihjklmnop") == 0


# Levenshtein.distance
def find_nearest_word3(word, dict_words):

    # Initial value
    if len(dict_words) == 0:
        print("No words in the dictionary.")
        return None

    minimal_edits = Levenshtein.distance(dict_words[0], word.lower())
    nearest_word = dict_words[0]
    for dict_word in dict_words:
        edits = Levenshtein.distance(dict_word, word.lower())
        if edits < minimal_edits:
            minimal_edits = edits
            nearest_word = dict_word
    return nearest_word


def find_nearest_word2(word, dict_words):

    # Initial value
    if len(dict_words) == 0:
        print("No words in the dictionary.")
        return None
    largest_common = common_letters(dict_words[0], word.lower())
    nearest_word = dict_words[0]
    for dict_word in dict_words:
        com = common_letters(dict_word, word.lower())
        if com > largest_common:
            largest_common = com
            nearest_word = dict_word
    return nearest_word


def find_nearest_word1(word, dict_words):
    basic_value = ascii_sum(word.lower())

    # Initial value
    if len(dict_words) == 0:
        print("No words in the dictionary.")
        return None

    nearest_word = dict_words[0]
    smallest_difference = abs(basic_value - ascii_sum(nearest_word))

    for dict_word in dict_words:
        diff = abs(basic_value - ascii_sum(dict_word))
        if diff < smallest_difference:
            smallest_difference = diff
            nearest_word = dict_word

    return nearest_word


user_input = input()
corrected1 = []
corrected2 = []
corrected3 = []

user_input_list = user_input.split(" ")
for word in user_input_list:
    if word.lower() in my_words:
        corrected1.append(word)
        corrected2.append(word)
        corrected3.append(word)
    else:
        corrected1.append(find_nearest_word1(word, my_words))
        corrected2.append(find_nearest_word2(word, my_words))
        corrected3.append(find_nearest_word3(word, my_words))

print(" ".join(corrected1))
print(" ".join(corrected2))
print(" ".join(corrected3))
