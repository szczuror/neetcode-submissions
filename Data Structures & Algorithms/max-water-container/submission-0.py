class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # literalnie asdy 2........................

        n = len(heights)
        current_max = 0

        left = 0
        right = n - 1
        while (left < right): 
            current_area = (right - left) * min(heights[left], heights[right])
            if current_area > current_max:
                current_max = current_area

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return current_max