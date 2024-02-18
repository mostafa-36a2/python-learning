from typing import List

# class Solution:
#     def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
#         from collections import defaultdict

#         actions_points = defaultdict(int)

#         for trip in trips:
#             actions_points[trip[1]] += trip[0]
#             actions_points[trip[2]] -= trip[0]

#         # actions_points = sorted(actions_points.items())

#         max_capacity = 0
#         currend_capacity = 0

#         for action_point in actions_points:
#             currend_capacity += action_point[1]
#             max_capacity = max(currend_capacity, max_capacity)
#         return max_capacity <= capacity

# from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from queue import PriorityQueue

        actions_points = PriorityQueue()

        for trip in trips:
            actions_points.put((trip[1], trip[0]))
            actions_points.put((trip[2], -trip[0]))

        max_capacity = 0
        current_capacity = 0

        while not actions_points.empty():
            next_item = actions_points.get()
            current_capacity += next_item[1]
            max_capacity = max(max_capacity, current_capacity)

        return max_capacity <= capacity


solution = Solution()
solution.carPooling(
    trips=[
        [1, 1, 2],
        [1, 1, 2],
        [1, 1, 2],
        [1, 1, 2],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
        [1, 0, 1],
    ],
    capacity=4,
)
