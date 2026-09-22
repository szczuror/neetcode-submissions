# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # for each node of root, check if the trees are the same

        def isSameTree(root: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
            q = deque([(root, root2)])

            while q:
                a, b = q.popleft()

                if not a and not b:
                    continue
                if not a or not b or a.val != b.val:
                    return False
                q.append((a.left, b.left))
                q.append((a.right, b.right))
            return True
        
        rq = deque([root])
        while rq:
            curr = rq.popleft()

            if curr.val == subRoot.val and isSameTree(curr, subRoot):
                return True

            if curr.left:
                rq.append(curr.left)
            if curr.right:
                rq.append(curr.right)

        return False        
