import random
from collections import Counter


def rock_paper_sessior():
    x = random.randint(0, 2)
    choices = {
        0: "rock",
        1: "sceissor",
        2: "paper",
    }
    print(choices[x])
    return choices[x]


rock_paper_sessior()


def start_with_random_number():
    x = random.randint(10000, 99999)

    def check_if_good(x):
        d = Counter(str(x))
        return len(d) >= 5

    while not check_if_good(x):
        x = random.randint(10000, 99999)
    print("Random number: ", x)
    return x


start_with_random_number()


def check_number(my_number, num: str):
    stars = 0
    bars = 0
    for c in num:
        real_position = my_number.find(c)
        opnt_position = num.find(c)
        if real_position == opnt_position:
            stars += 1
        elif real_position != -1:
            bars += 1
    print({"stars": stars, "bars": bars})
    return {"stars": stars, "bars": bars}


def test_check_number():
    assert check_number("01234", "56789") == {"stars": 0, "bars": 0}
    assert check_number("01234", "56784") == {"stars": 1, "bars": 0}
    assert check_number("01234", "56734") == {"stars": 2, "bars": 0}
    assert check_number("01234", "56234") == {"stars": 3, "bars": 0}
    assert check_number("01234", "56714") == {"stars": 1, "bars": 1}
    assert check_number("01234", "52134") == {"stars": 2, "bars": 2}
    assert check_number("01234", "10234") == {"stars": 3, "bars": 2}
    assert check_number("47025", "78329") == {"stars": 1, "bars": 1}
    assert check_number("47025", "47329") == {"stars": 3, "bars": 0}
    assert check_number("47025", "47025") == {"stars": 5, "bars": 0}
    assert check_number("81047", "84620") == {"stars": 1, "bars": 2}
    assert check_number("81047", "86379") == {"stars": 1, "bars": 1}
    assert check_number("81047", "84937") == {"stars": 2, "bars": 1}
    assert check_number("81047", "68937") == {"stars": 1, "bars": 1}
    assert check_number("81047", "80973") == {"stars": 1, "bars": 2}
    assert check_number("81047", "86034") == {"stars": 2, "bars": 1}
    assert check_number("81047", "86047") == {"stars": 4, "bars": 0}
    assert check_number("81047", "85047") == {"stars": 4, "bars": 0}
    assert check_number("81047", "86047") == {"stars": 5, "bars": 0}


assert check_number("82039", "82053") == {"stars": 5, "bars": 0}

# Try to guess
# a: 01234 *//
# b: 01235 //          [compare to a: We lost a star -> 4 is true, no bars added -> 5 is bad]
# c: 01264 */          [We lost a bar, 3 is bar, 6 is bad]
# d: 0 1 7 /3 *4 *///  [We got a new bar, 2 is bad, 7 is bar]
# : 0 1 /7 /3 *4 <- now we know this
# e: 0 8 /7 /3 *4 *///  [Nothing change, 1=8]
# f: 1 8 /7 /3 *4 *//// [we got a bar, compared to f, 0 is bad, 1 is in]
#  /1 /8 /7 /3 *4 <- now we know this
# g: 7   8   1   3 *4      **///
# h: 9  /8  *1  /3 *4      **//
#    3  7  *1  8  *4


# /0 x1  x2 /3  x4  //
# /0 x1  x2 /3   5  /// [a bar added, 4 is bad, 5 is in]
# /0 x1  x2 ?5   6  *//  [After d, we know 5 is star, but when added 6 instead of 3, 2 bars, no change -> 3=6]
# /0 x1  x2 /7   6  ///  [We lost a star, got a bar instead, 5 is in its place, 7 is in]
# /0 ?6  ?3 *5  ?7  **///
# *6 x1  ?3 *5  ?7  ***/  [We changed a bar to star, 6 is correct,0 not placed  ]
# *6 ?0  ?3 *5  ?7  ***//


# a# x0  x1  /2 *3  /4  *//
# b# x0  x1  /2 *3  x5  */  [Bar lost, 4 in, 5 out], after d => 2 and 3 are in, regarding c: 3 is star
# c# x0  x1  /2 /4  x6  //  [compared to a, we lost 3, 6 is out]
# d# x0  x1  *4 x6  /3  */ [since I'm sure or 4 and 3, 0 and 1 are out]
# e# x1  x6  *4 /2  /3 *//
# f#  /8  x7  *4 *3  /2 *//
# g#  /9  /8  *4 *3  /2
# h#  *2  *9  *4 *3 *8
