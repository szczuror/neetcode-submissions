class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = []
        i = j = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1
        if i == len(nums1) and j < len(nums2):
            while(j < len(nums2)):
                res.append(nums2[j])
                j += 1
        if j == len(nums2) and i < len(nums1):
            while(i < len(nums1)):
                res.append(nums1[i])
                i += 1

        idx = len(nums1) + len(nums2)

        if idx % 2 == 0:
            return (res[idx//2] + res[idx//2 - 1]) / 2
        
        return res[idx//2]