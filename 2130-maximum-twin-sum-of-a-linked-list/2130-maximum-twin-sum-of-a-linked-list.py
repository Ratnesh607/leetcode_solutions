# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        if head.next is None:
            return None 
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None
        
        prev = None
        curr = slow
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        first = head
        second = prev
        ans = 0
        while second:
            ans = max(ans, first.val + second.val)
            first = first.next
            second = second.next

        return ans
        