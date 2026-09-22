# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # watch out: there probably can be many group of K nodes fitting in the given list. Not just two like in the examples
        if not head:
            return head
        
        dummy = ListNode(0, head)
        prevG = dummy

        while True:
            kthNode = self.find_kth(prevG, k)
            if not kthNode:
                break
            next_node = kthNode.next

            # reversing k nodes
            prev,curr = kthNode.next, prevG.next
            while curr != next_node:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            # linking groups

            tmp = prevG.next
            prevG.next = kthNode
            prevG = tmp
        return dummy.next
    
    def find_kth(self, dummy: Optional[ListNode], k: int) -> Optional[ListNode]:
        i = 0
        curr = dummy
        while i < k and curr:
            i += 1
            curr = curr.next
        return curr