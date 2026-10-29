# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head

        curr = head
        prev = None
        n = 0
        while curr:
            n += 1
            prev = curr
            curr = curr.next

        k %= n
        if k == n or k == 0:
            return head

        curr = head
        for i in range(1, n - k):
            curr = curr.next

        new_head = curr.next
        curr.next = None
        prev.next = head
        return new_head
