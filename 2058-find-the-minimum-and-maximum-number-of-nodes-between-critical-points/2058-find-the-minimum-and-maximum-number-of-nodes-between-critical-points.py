# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        minDistance = float("inf")
        prev = head
        curr = head.next
        i = 1
        first = -1
        last = -1
        while curr.next:
            if ((curr.val < prev.val and curr.val < curr.next.val) or (curr.val > prev.val and curr.val > curr.next.val)):

                if first == -1:
                    first = i
                else:
                    minDistance = min(minDistance, i - last)
                last = i

            i += 1
            prev = curr
            curr = curr.next

        if first == -1 or first == last:
            return [-1, -1]

        maxDistance = last - first
        return [minDistance, maxDistance]