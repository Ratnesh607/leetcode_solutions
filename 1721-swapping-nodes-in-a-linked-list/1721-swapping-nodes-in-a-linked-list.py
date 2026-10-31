# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        n = 0
        while curr:
            n += 1
            curr = curr.next

        curr = head
        for i in range(k - 1):
            curr = curr.next

        first = curr

        curr = head
        for i in range(n - k):
            curr = curr.next

        first.val, curr.val = curr.val, first.val
        return head
        
