class Solution:
    def trap(self, height: List[int]) -> int:
        # O(n)
        result = 0
        n = len(height)

        left = 0
        right = n - 1
        left_max = height[left]
        right_max = height[right]

        while (left < right):
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        return result