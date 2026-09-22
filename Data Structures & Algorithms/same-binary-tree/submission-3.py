# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # bfs on both?
        if not p and not q:
            return True
        if (not p and q) or (p and not q):
            return False
        pqueue = deque([p])
        qqueue = deque([q])

        while pqueue or qqueue:
            if not pqueue and qqueue:
                return False
            if not qqueue and pqueue:
                return False

            currp = pqueue.popleft()
            currq = qqueue.popleft()
            if(currp.val != currq.val):
                return False
            
            if (currq.left and not currp.left) or (not currq.left and currp.left):
                return False
            if (currq.right and not currp.right) or (not currq.right and currp.right):
                return False

            if currp.left and currq.left:
                pqueue.append(currp.left)
                qqueue.append(currq.left)
            if currp.right and currq.right:
                pqueue.append(currp.right)
                qqueue.append(currq.right)

            
        return True