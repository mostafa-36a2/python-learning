from bisect import bisect_left, bisect_right
from typing import List

from sortedcollections import NearestDict


class MySortedStruct:
    def __init__(self, single_value: int):
        self.nearest_dict = NearestDict({single_value: 1})
        self.length = 1

    def get_smallest_diff_with(self, value) -> int:
        # Sorting the struct
        return abs(value - self.nearest_dict.nearest_key(value))

    def remove(self, value):
        val = self.nearest_dict[value]
        if val == 1:
            del self.nearest_dict[value]
        else:
            self.nearest_dict[value] = val - 1

    def add(self, value):
        nearest_value = self.nearest_dict.nearest_key(value)
        if nearest_value == value:  # Exact, increase
            val = self.nearest_dict[value]
            self.nearest_dict[value] = val + 1
        else:  # New value
            self.nearest_dict[value] = 1


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        # If valudDiff == 0, is is same as contains-duplicate-ii
        # If indexDiff >= len(nums), the whole list is included in search, no sliding

        MAX_WINDOW_SIZE = indexDiff + 1

        # Guranteed sorted struct, initial window with 1 item
        sorted_struct = MySortedStruct(nums[0])

        left_pointer = 0
        right_pointer = 1

        # Loop, O(n)
        while right_pointer < len(nums):
            diff = sorted_struct.get_smallest_diff_with(nums[right_pointer])

            if diff <= valueDiff:
                return True

            # Start removing the left most element in struct if the window size is maximum
            if sorted_struct.length == MAX_WINDOW_SIZE:
                sorted_struct.remove(nums[left_pointer])

            sorted_struct.add(nums[right_pointer])
            # Slide
            left_pointer += 1
            right_pointer += 1
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
