# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # bfs
        if not root:
            return 0
        
        dq = deque([root])

        lvl = 0
        while dq:
            level_size = len(dq)

            for i in range(level_size):
                node = dq.popleft()

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            lvl += 1
        return lvl