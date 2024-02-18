from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        buckets = {}
        bucket_size = valueDiff + 1

        for i, v in enumerate(nums):
            if i > indexDiff:
                index_to_remove = i - indexDiff - 1
                value_to_remove = nums[index_to_remove]
                bucket_id_of_value_to_remove = value_to_remove // bucket_size
                del buckets[bucket_id_of_value_to_remove]
            bucket_id = v // bucket_size

            if bucket_id in buckets:
                return True
            if (
                bucket_id - 1 in buckets
                and abs(buckets[bucket_id - 1] - v) <= valueDiff
            ):
                return True
            if (
                bucket_id + 1 in buckets
                and abs(buckets[bucket_id + 1] - v) <= valueDiff
            ):
                return True
            buckets[bucket_id] = v
        return False


# print(
#     Solution().containsNearbyAlmostDuplicate(
#         [7, 1, 3, 1, 2, 2, 3, 5, 6, 4, 2, 1, 2, 3, 4, 11, 16], indexDiff=1, valueDiff=5
#     )
# )
import os

path = os.path.join(os.path.dirname(__file__), "input_array.txt")
array = eval(open(path).read())
import time

start_time = time.time()
print(Solution().containsNearbyAlmostDuplicate(array, indexDiff=10000, valueDiff=0))
end_time = time.time()
print(end_time - start_time)
