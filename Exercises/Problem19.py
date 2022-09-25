# N Group
# Si students: 1<= Si <= 4
# Maximim in one Taxi is 4
# Find the minimum number of taxis
# Students from the same gourp MUST BE IN THE SAME TAXI
import math

input("Please enter the number of groups: ")
s = input()
# 1 1 1 2 2 2 3 3 3 4 4 4 4
counts = {4: s.count("4"), 3: s.count("3"), 2: s.count("2"), 1: s.count("1")}

# counts[1] = groups_of_1
# counts[2] = groups_of_2
# counts[3] = groups_of_3
# counts[4] = groups_of_4

count_of_taxis = 0

# [4]+4 ✅
print(f"we have found {counts[4]} of 4s.")
count_of_taxis += counts[4]
print(f"We have sent {counts[4]} of taxis for {counts[4]} groups of 4.")
counts[4] = 0

# [3 1]:min(3,1) ✅
print(f"we have found {counts[3]} of 3s, and {counts[1]} of 1s.")
minimum_of_3_and_1 = min(counts[3], counts[1])
count_of_taxis += minimum_of_3_and_1
counts[3] -= minimum_of_3_and_1
counts[1] -= minimum_of_3_and_1
print(
    f"We have sent {minimum_of_3_and_1} of taxis for {minimum_of_3_and_1} groups of 3s and {minimum_of_3_and_1} of 1s"
)

# [3 ?]+3 ✅
if counts[3] > 0:
    print(
        f"We still have {counts[3]} groups of 3s, that don't have groups of 1s to go with."
    )
    count_of_taxis += counts[3]
    print(f"We have sent {counts[3]} of taxis for {counts[3]} groups of 3s.")

# [2 2]:(2)//2 ✅
print(f"We have found {counts[2]} groups of 2s.")
count_of_taxis += counts[2] // 2
print(f"We have sent {counts[2]//2} of taxis for {counts[2]} groups of 2s.")
if counts[2] % 2 == 1:  # Odd
    counts[2] = 1
    print("Oops we still have one groups of 2 people, we will send it alone.")
    count_of_taxis += 1
    counts[2] = 0

    # [2 1 1]✅
    # [2 1 ?] ✅
    # [2 ? ?] ✅
    if counts[1] >= 2:
        counts[1] -= 2
    else:
        counts[1] = 0

# +ceil(groups of one)
# [1 1 1 1]✅
# [1 1 1 ?] ✅
# [1 1 ? ?] ✅
# [1 ? ? ?] ✅
print(f"We still have {counts[1]} if groups of 1s, remaining.")
count_of_taxis += math.ceil(counts[1] / 4)
print(f"We have sent {math.ceil(counts[1])} if taxis, for the remaining groups of 1s.")
print("The minimum taxis required is ", count_of_taxis)
