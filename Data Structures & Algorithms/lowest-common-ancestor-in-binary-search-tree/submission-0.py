# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # OR just bfs? and some fancy
        # this is a BST!!!

        pstack = []
        qstack = []

        curr = root
        while curr:
            if not curr:
                return None
            pstack.append(curr)
            if curr.val == p.val:
                break
            elif curr.val > p.val:
                curr = curr.left
            else:
                curr = curr.right
        
        curr = root
        while curr:
            if not curr:
                return None
            qstack.append(curr)
            if curr.val == q.val:
                break
            elif curr.val > q.val:
                curr = curr.left
            else:
                curr = curr.right
        if p in qstack:
            return p
        if q in pstack:
            return q
        
        lca = root
        for node_p, node_q in zip(pstack, qstack):
            if node_p == node_q:
                lca = node_p
            else:
                break

        return lca
