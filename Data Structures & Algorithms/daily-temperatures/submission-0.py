class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = [] # it stores: temperatue, index

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((temp, i))
        
        return res
