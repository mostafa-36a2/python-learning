"""
Resources:

Explanation:
https://www.youtube.com/watch?v=wJUjIdS23U0


Problem link:
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/submissions/1159969867/?envType=daily-question&envId=2024-01-28

Medium level:
https://leetcode.com/problems/subarray-sum-equals-k/description/

All prefix sum problems:
https://leetcode.com/tag/prefix-sum/

Tutorials:
https://leetcodethehardway.com/tutorials/basic-topics/prefix-sum

Discussions and study guide:
https://leetcode.com/discuss/study-guide/4023666/prefix-sum-questions-to-practice

Geeks for Geeks implementation
https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/

"""
from typing import List

debug = False


def pprint(matrix):
    print("[")
    for row, value in enumerate(matrix):
        print("  ", value)
    print("]")


# matrix = [
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
#     [1, 1, 1, 1],
# ]


# matrix_global = [
#     [00, 01, 02, 03],
#     [10, 11, 12, 13],
#     [20, 21, 22, 23],
#     [30, 31, 32, 33],
#     [40, 41, 42, 43],
# ]


def calc_2d_prefix(matrix):
    HEIGHT = len(matrix)
    WIDTH = len(matrix[0])
    if debug:
        print(f"HEIGHT={HEIGHT}, WIDTH={WIDTH}")
    for row_id in range(HEIGHT - 1, -1, -1):
        for col_id in range(WIDTH - 1, -1, -1):
            # Last row
            if col_id == WIDTH - 1 and row_id == HEIGHT - 1:
                pass
            elif col_id == WIDTH - 1:
                matrix[row_id][col_id] += matrix[row_id + 1][col_id]
            elif row_id == HEIGHT - 1:
                matrix[row_id][col_id] += matrix[row_id][col_id + 1]
            else:
                matrix[row_id][col_id] = (
                    matrix[row_id][col_id]
                    + matrix[row_id + 1][col_id]
                    + matrix[row_id][col_id + 1]
                    - matrix[row_id + 1][col_id + 1]
                )


def get_sum(matrix, row1, col1, row2, col2):
    """
    matrix is the prefix sum
    """
    HEIGHT = len(matrix)
    WIDTH = len(matrix[0])

    # if row1 == HEIGHT - 1 and col1 == WIDTH - 1:
    #     # For sure, row1==row2, col1==col2
    #     return matrix[row1][col1]
    # if row1 == HEIGHT - 1:
    #     # For sure, row1==row2
    #     return matrix[row1][col1] - matrix[row1][col2 + 1]
    # if col1 == WIDTH - 1:
    #     # For sure, col1==col2
    #     return matrix[row1][col1] - matrix[row2 + 1][col1]

    if row2 == HEIGHT - 1 and col2 == WIDTH - 1:
        return matrix[row1][col1]
    if row2 == HEIGHT - 1:
        return matrix[row1][col1] - matrix[row1][col2 + 1]
    if col2 == WIDTH - 1:
        return matrix[row1][col1] - matrix[row2 + 1][col1]

    return (
        matrix[row1][col1]
        - matrix[row1][col2 + 1]
        - matrix[row2 + 1][col1]
        + matrix[row2 + 1][col2 + 1]
    )


# assert (res := get_sum(0, 0, 1, 1)) == 4, res
# assert (res := get_sum(1, 1, 3, 3)) == 9, res
# assert (res := get_sum(2, 2, 3, 3)) == 4, res
# assert (res := get_sum(0, 0, 3, 3)) == 16, res


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        from collections import defaultdict

        if debug:
            pprint(matrix)
        calc_2d_prefix(matrix)

        if debug:
            pprint(matrix)

        count = 0
        for row1, _ in enumerate(matrix):
            for row2 in range(row1, len(matrix)):
                if debug:
                    print(f"Scanning between row:{row1} and row:{row2}")
                d = defaultdict(int)
                for col1, _ in enumerate(matrix[row1]):
                    if debug:
                        print(f"    Scanning between col:0 and col:{col1}")
                    current_sum = get_sum(matrix, row1, 0, row2, col1)
                    other = current_sum - target
                    if debug:
                        print(
                            f"\t\tcurrent_sum:({current_sum}) , other:({other}), d:{dict(d)}"
                        )
                    # First iteration
                    if current_sum == target:
                        count += 1
                    if other in d:
                        count += d[other]
                    d[current_sum] += 1
                    if debug:
                        print(f"\t\tcount={count} , d={dict(d)}")
        return count


# if debug:
#     print(
#         Solution().numSubmatrixSumTarget(
#             matrix=[[0, 1, 0], [1, 1, 1], [0, 1, 0]], target=0
#         )
#     )

# if debug:
#     print(Solution().numSubmatrixSumTarget(matrix=[[1, -1], [-1, 1]], target=0))

if debug or True:
    import os

    print(
        Solution().numSubmatrixSumTarget(
            matrix=eval(
                open(
                    os.path.join(os.path.dirname(__file__), "input_matrix.txt"), "r"
                ).read()
            ),
            target=-3500,
        )
    )
