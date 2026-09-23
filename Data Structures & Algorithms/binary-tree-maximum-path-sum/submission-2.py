# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # recurrency: 
        # max from: currnode, currnode + leftMax, currNode+rightMax
        res = -float('inf')
        def maxSum(root):
            nonlocal res
            if not root:
                return 0
            
            left_gain = max(0, maxSum(root.left))
            right_gain = max(0, maxSum(root.right))

            res = max(res, root.val + right_gain + left_gain)

            return root.val + max(left_gain, right_gain)
        
        maxSum(root)

        return res