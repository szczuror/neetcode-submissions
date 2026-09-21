# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recurrent approach
        result = 0

        def dfs(root):
            nonlocal result
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            result = max(left + right, result)

            return 1 + max(left, right)

        dfs(root)
        return result