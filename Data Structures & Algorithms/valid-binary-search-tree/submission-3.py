# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validRec(node: Optional[TreeNode], minVal, maxVal) -> bool:
            if not node:
                return True
            curr = node.val

            if curr <= minVal or curr >= maxVal:
                return False
            
            return validRec(node.left, minVal, curr) and validRec(node.right, curr, maxVal)

        return validRec(root, -float('inf'), float('inf'))