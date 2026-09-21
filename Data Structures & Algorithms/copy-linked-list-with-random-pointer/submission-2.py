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
        nodes = {} # mapping of relations, as next and random nodes may not exist during first creation cycle

        curr = head
        while curr: # initial copying, without nexts and randoms
            copy = Node(curr.val)
            nodes[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = nodes[curr] # copy that was made.
            copy.next = nodes.get(curr.next) # linking to a nodes
            copy.random = nodes.get(curr.random)
            curr = curr.next

        return nodes[head]