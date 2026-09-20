class Solution:
    def findMin(self, nums: List[int]) -> int:
        # partially sorted. 
        # first step is to find the rotation point

        left, right = 0, len(nums) - 1

        
        pivot = 0
        while left < right:
            mid = (left + right) // 2

            if (nums[mid] < nums[right]):
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
