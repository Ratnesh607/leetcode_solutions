# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(0)
        curr = ans
        carry = 0

        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a + b + carry
            curr.next = ListNode(total % 10)
            curr = curr.next
            carry = total // 10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return ans.next