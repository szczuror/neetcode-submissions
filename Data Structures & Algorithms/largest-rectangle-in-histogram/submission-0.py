class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 # initial max height

        # create a stack that holds indexes so that we can calculate area 
        for idx, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                
                width = idx - left - 1
                max_area = max(max_area, width * h)
            stack.append(idx)
        
        while stack:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = len(heights) - left - 1
            max_area = max(max_area, width * h)
            
        return max_area