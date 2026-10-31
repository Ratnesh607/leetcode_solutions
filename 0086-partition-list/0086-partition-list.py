# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        small = ListNode(0)
        large = ListNode(0)
        p1 = small
        p2 = large
        curr = head
        while curr:
            if curr.val < x:
                p1.next = curr
                p1 = p1.next
            else:
                p2.next = curr
                p2 = p2.next

            curr = curr.next

        p2.next = None
        p1.next = large.next
        return small.next
        
        