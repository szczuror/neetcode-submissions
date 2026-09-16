class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0

        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            curr = 1
            if ((num - 1) in nums_set):
                continue
            # try from this then
            currnum = num
            while ((currnum + 1) in nums_set):
                currnum += 1
                curr += 1
            longest = max(longest, curr)
        return longest