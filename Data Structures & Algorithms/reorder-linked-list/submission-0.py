# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        slow, fast = head, head.next

        while fast and fast.next: # this allows us to find the middle of linked list
            slow = slow.next
            fast = fast.next.next 

        second = slow.next
        previous = slow.next = None

        while second:
            tmp = second.next

            second.next = previous
            previous = second
            second = tmp
        # second list is now reversed

        first, second = head, previous # starts of both lists

        while second:
            tmp1, tmp2 = first.next, second.next

            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        