# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # recursevily get down with max val

        result = 0

        def dfs(root, max_value):
            nonlocal result

            if not root:
                return 0
            
            if root.val >= max_value:
                result += 1
            max_value = max(max_value, root.val)

            dfs(root.left, max_value)
            dfs(root.right, max_value)
        
        dfs(root, root.val)

        return result