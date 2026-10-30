# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        ans = head.next
        prev = None
        curr = head

        while curr and curr.next:
            sec = curr.next
            nextNode = sec.next
            sec.next = curr
            curr.next = nextNode
            if prev:
                prev.next = sec

            prev = curr
            curr = nextNode
        return ans