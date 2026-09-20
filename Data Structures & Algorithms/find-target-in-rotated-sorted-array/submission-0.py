class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1

        left, right = 0, len(nums) - 1

        # search for a pivot then do a search on valid array?
        pivot = -1
        while left < right:
            mid = (left + right) // 2

            if (nums[mid] > nums[right]):
                left = mid + 1
            else:
                right = mid
        
        pivot = left

        def binsearch(left, right):
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        
        return binsearch(0, pivot - 1) if (binsearch(0, pivot - 1) != -1) else binsearch(pivot, len(nums) - 1)