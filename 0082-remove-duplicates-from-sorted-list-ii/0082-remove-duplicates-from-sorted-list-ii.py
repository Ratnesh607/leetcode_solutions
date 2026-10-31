class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head

        while head and head.next and head.val == head.next.val:
            val = head.val
            while head and head.val == val:
                head = head.next

        if not head:
            return None

        prev = head
        curr = head.next
        while curr:
            if curr.next and curr.val == curr.next.val:
                val = curr.val
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return head        