from typing import List


class Interval:
    deleted: bool
    start: int
    end: int

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.deleted = False


def is_overlap(left_interval, right_interval):
    """
    >>> is_overlap([0,10],[10,12])
    False
    >>> is_overlap([0,11],[10,12])
    True
    >>> is_overlap([0,11],[5,7])
    True
    >>> is_overlap([0,4],[5,7])
    False
    >>> is_overlap([1,2],[1,2])
    True
    """
    # The right interval starts before the left interval ends
    return right_interval[0] < left_interval[1]


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1,2],[2,3],[3,4],[1,3]
        # [0,1,2,3,4]

        # [0,1,1,0,0]
        # [0,0,1,1,0]
        # [0,0,0,1,1]
        # [0,1,1,1,1]
        # Step1: Sort intervals by lower start, lower end
        # Step2: Loop through intervals
        #    Step2.1: Loop through intervals after the current one
        #    Step2.2: Check if overlap? remove the one that ends later
        #    Step2.3: If the one that you have removed is the current one, break
        sorted_intervals = sorted(intervals)
        num_of_removed = 0
        for index, curr_interval in enumerate(sorted_intervals):
            if curr_interval[0] is None:
                continue
            for other in range(index + 1, len(sorted_intervals)):
                other_interval = sorted_intervals[other]
                if other_interval[0] is None:
                    continue
                if is_overlap(curr_interval, other_interval):
                    num_of_removed += 1
                    if curr_interval[1] < other_interval[1]:
                        sorted_intervals[other][0] = None
                        sorted_intervals[other][1] = None
                    else:
                        curr_interval[0] = None
                        curr_interval[1] = None
                        # Current one deleted
                        break
                else:
                    # No more overlappings
                    break
        return num_of_removed


# input_list = [[1, 2], [1, 2], [1, 2]]
# print(Solution().eraseOverlapIntervals(input_list))
