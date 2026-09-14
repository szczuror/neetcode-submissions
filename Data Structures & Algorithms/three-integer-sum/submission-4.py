class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # not returning indices but nums[x] triplets
        # triplets which sum exactly to 0
        # O(n^2)
        nums = sorted(nums) # O(nlogn)
        # for each pivot find two more ig
        result = []

        n = len(nums)

        for i in range(n):
            current_num = nums[i]
            
            if i > 0 and nums[i] == nums[i - 1]: # eliminating some duplicates
                continue

            left = i + 1
            right = n - 1
            while (left < right):
                res = current_num + nums[left] + nums[right]
                if (res == 0):
                    result.append((current_num, nums[left], nums[right]))
                    left += 1
                    right -= 1
                # eliminate duplicates
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif res < 0:
                    left += 1
                else:
                    right -= 1
        return result