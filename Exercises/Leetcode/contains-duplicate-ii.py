from typing import List


class Number:
    value: int
    index: int

    def __init__(self, index, value):
        self.index = index
        self.value = value

    def __repr__(self):
        return f"({self.index}, {self.value})"


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        numbers = [Number(index, value) for index, value in enumerate(nums)]
        numbers.sort(key=lambda n: (n.value, n.value))
        len_nums = len(nums)
        left_index = 0
        # For each number
        while left_index < len(numbers) - 1:
            # Pick number
            left_number = numbers[left_index]
            right_index = left_index + 1
            # should be valid index
            # if right_index < len(numbers):
            right_number = numbers[right_index]

            if abs(left_number.value, right_number.value) <= valueDiff:
                if abs(left_number.index, right_number.index) <= indexDiff:
                    return True
                else:
                    # Skip the right value because all other indexes of same value are larger
                    while (
                        right_index < len_nums
                        and numbers[right_index].value == right_number.value
                    ):
                        right_index += 1
            else:
                # Oops, all the right values will be worst. skip the value
                while (
                    left_index < len_nums
                    and numbers[left_index].value == left_number.value
                ):
                    left_index += 1
        return False


print(Solution().containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3))
