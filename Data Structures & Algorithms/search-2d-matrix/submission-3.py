class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        # The first integer of every row is greater than the last integer of the previous row.
        # so -- first a binary search on rows maybe, and if we find a good row then on the columns (so, elements of the row)

        left, right = 0, rows - 1
        
        target_row = 0
        while left <= right:
            mid = (left + right) // 2

            curr_left = matrix[mid][0]
            curr_right = matrix[mid][cols - 1]

            if curr_left <= target <= curr_right:
                target_row = mid
                break
            elif curr_left > target:
                right = mid - 1
            elif curr_right < target:
                left = mid + 1
        
        # now binary search but on just this found row

        left_second, right_second = 0, cols - 1

        while left_second <= right_second:
            mid = (left_second + right_second) // 2
            
            value = matrix[target_row][mid]

            if value == target:
                return True
            elif value > target:
                right_second = mid - 1
            else:
                left_second = mid + 1
        return False