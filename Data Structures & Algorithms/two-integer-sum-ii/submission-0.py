class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 1-indexed for some reason
        diffs = {}
        n = len(numbers) - 1
        left = 0
        right = n
        
        # array is sorted!
        while (left < right):
            current_res = numbers[left] + numbers[right]
            if (current_res == target):
                return [left + 1, right + 1]
            elif current_res < target:
                left += 1
            else:
                right -= 1