from typing import List


def difference_between_two_nearest_values(my_list: list):
    my_list.sort()
    min_dif = float("inf")
    # pair = (None, None)
    for i in range(1, len(my_list)):
        if min_dif > abs(my_list[i] - my_list[i - 1]):
            # pair = (l[i], l[i - 1])
            min_dif = abs(my_list[i] - my_list[i - 1])
    return min_dif


def has_2_numbers_within_valueDiff_distance(sub_nums, valueDiff):
    diff = difference_between_two_nearest_values(sub_nums)
    if diff <= valueDiff:
        # We have found 2 numbers with distance < indexDiff
        # And they have difference <= valueDiff
        return True
    return False


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        # If valudDiff == 0, is is same as contains-duplicate-ii
        # If indexDiff >= len(nums), the whole list is included in search, no sliding

        if indexDiff >= len(nums):
            return has_2_numbers_within_valueDiff_distance(nums, valueDiff)
        # Sliding window
        for leftmost in range(0, len(nums) - indexDiff):
            sub_nums = nums[leftmost : leftmost + indexDiff + 1]
            print(f"New window between indeces [{leftmost}, {leftmost + indexDiff}]")
            # print(f"Sub array: {sub_nums}")
            if has_2_numbers_within_valueDiff_distance(sub_nums, valueDiff):
                return True
        return False


# print(Solution().containsNearbyAlmostDuplicate([1, 2, 1, 1], indexDiff=1, valueDiff=0))
import os

path = os.path.join(os.path.dirname(__file__), "input_array.txt")
array = eval(open(path).read())
import time

start_time = time.time()
print(Solution().containsNearbyAlmostDuplicate(array, indexDiff=10000, valueDiff=0))
end_time = time.time()
print(end_time - start_time)
