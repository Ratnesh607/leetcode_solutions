class Solution:
    def resultArray(self, nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
        n = len(nums)
        tree = [([0] * k, 0) for _ in range(4 * n)]
        def merge(left, right):
            cnt = left[0].copy()
            prod = (left[1] * right[1]) % k
            for x in range(k):
                newRem = (left[1] * x) % k
                cnt[newRem] += right[0][x]
            return (cnt, prod)

        def build(i, l, r):
            if l == r:
                rem = nums[l] % k
                tree[i] = ([0] * k, rem)
                tree[i][0][rem] = 1
                return

            mid = (l + r) // 2
            build(2 * i + 1, l, mid)
            build(2 * i + 2, mid + 1, r)
            tree[i] = merge(tree[2 * i + 1], tree[2 * i + 2])

        def update(i, l, r, index, value):
            if l == r:
                rem = value % k
                tree[i] = ([0] * k, rem)
                tree[i][0][rem] = 1
                return

            mid = (l + r) // 2
            if index <= mid:
                update(2 * i + 1, l, mid, index, value)
            else:
                update(2 * i + 2, mid + 1, r, index, value)
            tree[i] = merge(tree[2 * i + 1], tree[2 * i + 2])

        def query(start, end, i, l, r):
            if start <= l and r <= end:
                return tree[i]

            mid = (l + r) // 2
            if end <= mid:
                return query(start, end, 2 * i + 1, l, mid)
            if start > mid:
                return query(start, end, 2 * i + 2, mid + 1, r)
            left = query(start, end, 2 * i + 1, l, mid)
            right = query(start, end, 2 * i + 2, mid + 1, r)
            return merge(left, right)
        build(0, 0, n - 1)
        result = []

        for q in queries:
            index = q[0]
            value = q[1]
            start = q[2]
            x = q[3]
            update(0, 0, n - 1, index, value)
            node = query(start, n - 1, 0, 0, n - 1)
            result.append(node[0][x])
        return result