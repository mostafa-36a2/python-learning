from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         from sortedcontainers import SortedList

#         left_pointer = 0
#         sorted_prices = SortedList(prices[1:], key=lambda x: -x)

#         max_diff = 0

#         for right_pointer in range(1, len(prices)):
#             left_number = prices[left_pointer]
#             right_number = sorted_prices[0]
#             # print(f"Compraing {left_number} with {right_number}")
#             max_diff = max(max_diff, right_number - left_number)
#             left_pointer += 1
#             sorted_prices.remove(prices[right_pointer])
#         return max_diff


def recurs(prices: List[int]):
    """
    Return max, min, max_diff
    """
    if len(prices) == 1:
        return prices[0], prices[0], 0
    else:
        half_len = len(prices) // 2
        half_left = prices[:half_len]
        half_right = prices[half_len:]
        mx_left, mn_left, df_left = recurs(half_left)
        mx_right, mn2_right, df2_right = recurs(half_right)
        return (
            max(mx_left, mx_right),
            min(mn_left, mn2_right),
            max(max(df_left, df2_right), mx_right - mn_left),
        )


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return recurs(prices)[2]


print(Solution().maxProfit(prices=[7, 1, 5, 3, 6, 4]))
