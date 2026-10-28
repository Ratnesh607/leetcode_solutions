# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        ans = ListNode(0)
        curr = ans
        carry = 0
        while prev or carry:
            a = prev.val if prev else 0
            a = a * 2 + carry
            curr.next = ListNode(a % 10)
            curr = curr.next
            carry = a // 10
            if prev:
                prev = prev.next

        prev = None
        curr = ans.next
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev