from typing import List
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        tree = [0] * (4 * n)
        square = [0] * (4 * n)
        lazy = [0] * (4 * n)
        def apply(node, start, end, val):
            length = end - start + 1
            square[node] = (
                square[node] + 2 * val * tree[node]
                + length * val * val
            ) % mod

            tree[node] = (tree[node] + length * val) % mod
            lazy[node] += val

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            mid = (start + end) // 2
            val = lazy[node]
            apply(node * 2, start, mid, val)
            apply(node * 2 + 1, mid + 1, end, val)
            lazy[node] = 0

        def update(node, start, end, left, right):
            if right < start or end < left:
                return

            if left <= start and end <= right:
                apply(node, start, end, 1)
                return

            push(node, start, end)
            mid = (start + end) // 2
            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)
            tree[node] = (
                tree[node * 2] + tree[node * 2 + 1]
            ) % mod
            square[node] = (
                square[node * 2] + square[node * 2 + 1]
            ) % mod

        last = {}
        ans = 0
        for i in range(n):
            prev = last.get(nums[i], -1)
            update(1, 0, n - 1, prev + 1, i)
            ans = (ans + square[1]) % mod
            last[nums[i]] = i
        return ans