from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        frequency_rows = [set() for _ in range(9)]
        frequency_cols = [set() for _ in range(9)]
        frequency_subboxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue

                box_idx = (i // 3) * 3 + (j // 3)

                if (val in frequency_rows[i]
                    or val in frequency_cols[j]
                    or val in frequency_subboxes[box_idx]
                ):
                    return False

                frequency_rows[i].add(val)
                frequency_cols[j].add(val)
                frequency_subboxes[box_idx].add(val)

        return True