# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # recurrent approach
        # we go down nodes and return max(height(node.left), height(node.right)) + 1
        res = True
        def heights(root: Optional[TreeNode]) -> int:
            nonlocal res
            if not root:
                return 0
            
            leftHeight = heights(root.left)
            rightHeight = heights(root.right)

            if abs(leftHeight - rightHeight) > 1:
                res = False

            return max(leftHeight, rightHeight) + 1

        heights(root)
        return res