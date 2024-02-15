from typing import List

from sortedcontainers import SortedList

DEBUG = False


class MySortedStruct:
    def __init__(self, single_value: int):
        self.sorted_list = SortedList([single_value])
        self.length = 1

    def get_smallest_diff_with(self, value) -> int:
        left_index = self.sorted_list.bisect_left(value)
        right_index = self.sorted_list.bisect_right(value)
        if DEBUG:
            print(left_index, right_index)
        # If the item dosn't exist, left_index == right_index
        if left_index == right_index:
            if left_index == 0:
                return self.sorted_list[left_index] - value

            if right_index == self.length:
                return value - self.sorted_list[-1]
            # Value is in the middle
            return min(
                value - self.sorted_list[left_index - 1],
                self.sorted_list[left_index] - value,
            )
        else:
            # Value exist before wow!
            return 0

    def remove(self, value):
        self.sorted_list.remove(value)
        self.length -= 1

    def add(self, value):
        self.sorted_list.add(value)
        self.length += 1


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
            # Start removing the left most element in struct if the window size is maximum
            if sorted_struct.length == MAX_WINDOW_SIZE:
                sorted_struct.remove(nums[left_pointer])
                left_pointer += 1

            if DEBUG:
                print(
                    f"Testing window {sorted_struct.sorted_list} for {nums[right_pointer]}"
                )

            diff = sorted_struct.get_smallest_diff_with(nums[right_pointer])

            if DEBUG:
                print(f"Smallest difference is {diff}")

            if diff <= valueDiff:
                # print(
                #     f"Diff: {diff}, sorted_struct={sorted_struct.sorted_list}, value={nums[right_pointer]}"
                # )
                return True

            sorted_struct.add(nums[right_pointer])

            # Slide
            right_pointer += 1
        return False


print(
    Solution().containsNearbyAlmostDuplicate(
        [7, 1, 3, 1, 2, 2, 3], indexDiff=1, valueDiff=0
    )
)
# import os

# path = os.path.join(os.path.dirname(__file__), "input_array.txt")
# array = eval(open(path).read())
# import time

# start_time = time.time()
# print(Solution().containsNearbyAlmostDuplicate(array, indexDiff=10000, valueDiff=0))
# end_time = time.time()
# print(end_time - start_time)
