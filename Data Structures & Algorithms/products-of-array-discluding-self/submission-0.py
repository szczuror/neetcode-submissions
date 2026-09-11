class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * n
        suffix_prod = [1] * n

        prefix_prod[0] = nums[0]
        for i in range(1, n):
            prefix_prod[i] = nums[i] * prefix_prod[i-1]

        suffix_prod[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_prod[i] = nums[i] * suffix_prod[i+1]

        ans = []
        for idx, num in enumerate(nums):
            left = prefix_prod[idx - 1] if idx > 0 else 1
            right = suffix_prod[idx + 1] if idx < n - 1 else 1

            ans.append(left * right)
        return ans
        