# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        ans = 0
        i = 0
        j = len(arr) - 1
        while i < j:
            ans = max(ans, arr[i] + arr[j])
            i += 1
            j -= 1

        return ans
        