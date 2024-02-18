from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        memo_res = {}
        for index, day_temp in enumerate(temperatures):
            distance = 0
            cycles = 0

            if index < memo_res.get(day_temp, index):
                distance = memo_res[day_temp] - index
            elif memo_res.get(day_temp) == -1:
                distance = 0
            else:
                for other_idx in range(index + 1, len(temperatures)):
                    cycles += 1
                    if day_temp < temperatures[other_idx]:
                        distance = other_idx - index
                        memo_res[day_temp] = other_idx
                        break
                if distance == 0:
                    memo_res[day_temp] = -1
            res.append(distance)
        return res


import os

print(
    Solution().dailyTemperatures(
        temperatures=eval(
            open(
                os.path.join(os.path.dirname(__file__), "input-array-2.txt"), "r"
            ).read()
        )
    )
)
