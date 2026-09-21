"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        # copied_head = Node(x=head.val, next=head.next, random=head.random)

        nodes = {None : None}

        curr = head
        while curr: # initial copying, without nexts and randoms
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = nodes[curr] # copy that was made.
            copy.next = nodes[curr.next] # linking to a nodes
            copy.random = nodes[curr.random]
            curr = curr.next

        return nodes[head]