import random
from argparse import ArgumentParser
from collections import Counter


def get_arguments():
    parser = ArgumentParser()
    parser.add_argument(
        "--player",
        type=int,
        dest="player",
        help=f"The player number",
        required=True,
    )
    arguments = parser.parse_args()

    return arguments.player


player = get_arguments()


def rock_paper_sessior():
    x = random.randint(0, 2)
    choices = {
        0: "rock",
        1: "sceissor",
        2: "paper",
    }
    print(choices[x])
    return choices[x]


def get_random_valid_number():
    x = random.randint(10000, 99999)

    def check_if_good(x):
        d = Counter(str(x))
        return len(d) >= 5

    while not check_if_good(x):
        x = random.randint(10000, 99999)
    print("Random number: ", x)
    return x


# 39458
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


def unit_test_check_number():
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


current_guess = ["?", "?", "?", "?", "?", "?", "?", "?", "?", "?"]


def cmp_rslts_sbst_1_strtgy(old_digit, res1, new_digit, res2):
    old_digit = int(old_digit)
    new_digit = int(new_digit)
    # Only Bars changed
    if res1["stars"] == res2["stars"] and res1["bars"] > res2["bars"]:
        current_guess[old_digit] = "/"
        current_guess[new_digit] = "x"
        print(f"{old_digit} is bar, {new_digit} is out")
    elif res1["stars"] == res2["stars"] and res1["bars"] < res2["bars"]:
        current_guess[old_digit] = "x"
        current_guess[new_digit] = "/"
        print(f"{old_digit} is out, {new_digit} is bar")
    # Only Stars changed
    elif res1["stars"] > res2["stars"] and res1["bars"] == res2["bars"]:
        current_guess[old_digit] = "*"
        current_guess[new_digit] = "x"
        print(f"{old_digit} is star, {new_digit} is out")
    elif res1["stars"] < res2["stars"] and res1["bars"] == res2["bars"]:
        current_guess[old_digit] = "x"
        current_guess[new_digit] = "*"
        print(f"{old_digit} is out,{new_digit} is star")
    # Stars and bars changed
    # less bars, more stars
    elif res1["stars"] > res2["stars"] and res1["bars"] < res2["bars"]:
        current_guess[old_digit] = "/"
        current_guess[new_digit] = "*"
        print(f"{old_digit} was bar, {new_digit} is star")
    # less stars, more bars
    elif res1["stars"] < res2["stars"] and res1["bars"] > res2["bars"]:
        current_guess[old_digit] = "*"
        current_guess[new_digit] = "/"
        print(f"{old_digit} was star,{new_digit} is bar")
    # Nothing changed
    elif res1["stars"] == res2["stars"] and res1["bars"] == res2["bars"]:
        current_guess[old_digit] = f"As {new_digit}"
        current_guess[new_digit] = f"As {old_digit}"
        print(f"{old_digit} = {new_digit}")
    # ERROR< CASE NOT HANDLED
    else:
        print("Not handled case.")

    return current_guess[old_digit], current_guess[new_digit]


def ask_to_evaluate_number(num):
    res = input(num)  # ////
    return {"stars": res.count("*"), "bars": res.count("/")}


def get_other_unknown(current_guess_list, not_this_one, last_guess=None):
    for idx, val in enumerate(current_guess_list):
        if val == "?" and idx != not_this_one:
            if last_guess:
                if str(idx) not in last_guess:
                    return idx
            else:
                return idx
    return None


assert get_other_unknown(list("??????????"), 0) == 1
assert get_other_unknown(list("??????????"), 1) == 0
assert get_other_unknown(list("x?????????"), 1) == 2
assert get_other_unknown(list("xxxxxxxx??"), 8) == 9
assert get_other_unknown(list("xxx?xxx???"), 3) == 7


def get_next_guess(current_guess_list, last_guess, change_only=1):
    output = ""
    for c in last_guess:
        o = c
        if change_only:
            if current_guess_list[int(c)] == "?":
                o = get_other_unknown(current_guess_list, int(c), last_guess)
                if o == None:
                    # print("Error, can't choose a new number :(")
                    return None
                change_only -= 1
        output += str(o)
    return output


assert get_next_guess(list("??????????"), "02457") == "12457"
assert get_next_guess(list("??????????"), "12457") == "02457"
assert get_next_guess(list("x?????????"), "12457") == "32457"
assert get_next_guess(list("xxxxxxxx??"), "82457") == "92457"
assert get_next_guess(list("xxx?xxx???"), "32457") == "82457"
assert get_next_guess(list("xxx?xxx???"), "98736") == None


def find_old(old_num, new_num):
    old_num = str(old_num)
    new_num = str(new_num)
    for idx, val in enumerate(old_num):
        if val != new_num[idx]:
            return val


def find_new(old_num, new_num):
    old_num = str(old_num)
    new_num = str(new_num)
    for idx, val in enumerate(old_num):
        if val != new_num[idx]:
            return new_num[idx]


def try_to_guess():
    print("Staring try_to_guess function ...")
    old_number = get_random_valid_number()  # 19524
    old_result = ask_to_evaluate_number(old_number)
    print("Result: ", old_result)
    for i in range(4):
        new_num = get_next_guess(current_guess, str(old_number))
        new_res = ask_to_evaluate_number(new_num)

        cmp_res = cmp_rslts_sbst_1_strtgy(
            find_old(old_number, new_num),
            old_result,
            find_new(old_number, new_num),
            new_res,
        )
        print(current_guess)
        old_number = new_num
        old_result = new_res


if player == 1:
    try_to_guess()
    # After try_to_guess, only 2 numbers are in '?' state;
    exit()

else:
    rock_paper_sessior()
    my_random_number = get_random_valid_number()
    print("My random number is: ", my_random_number)
    my_random_number = 25109
    game_loop = True
    while game_loop:
        num = input("Please enter a number: ")
        res = check_number(str(my_random_number), num)
        if str(my_random_number) == num:
            game_loop = False
    print("Thank you")

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

res = input("12345")  # */
res = input("12346")  # *//
# if bars increased: 6 in, 5 out
res = input("12367")  # *//   [4=7]
res = input("12647")  # **/  seems that no 3, no 4 or 7, 126 are in
res = input("02647")  # Strategy: change one number
# (From **/ to *//, 1 was star, 0 is bar, 2 is bar, 6 is star)
res = input("10628")  # ***/
res = input("19628")  # **// (0 was star, 9 is bar)
res = input("10692")  # *****


#######################

res1 = input("12345")  # ///
res2 = input("12346")  # /// [5=6]**
res3 = input("12376")  # /// [4=7]
res4 = input("12876")  # /// [3=8]**
res5 = input("19876")  # // 2 is bar, 9 is out
res6 = input("09876")  # // [1=0]
res7 = input("83561")  # ****
res8 = input("83562")  # *****


res1 = input("12345")  # ///
res2 = input("12346")  # /// [5=6]**
res3 = input("12376")  # /// [4=7]
res4 = input("12876")  # /// [3=8]**
res5 = input("19876")  # // 2 is bar, 9 is out
res6 = input("09876")  # // [1=0]
res7 = input("83561")  # ****
res8 = input("83562")  # *****
