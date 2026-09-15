class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        if n % 2 != 0:
            return False
        
        bmap = {"{":"}", 
               "(" : ")",
               "[" : "]"}
        stack = []

        for char in s:
            if char in bmap:
                stack.append(char)
            else:
                if not stack or bmap[stack.pop()] != char:
                    return False
        return len(stack) == 0