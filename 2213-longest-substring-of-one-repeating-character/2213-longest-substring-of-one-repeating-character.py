class Solution:
    def longestRepeating(
        self,
        s: str,
        queryCharacters: str,
        queryIndices: List[int]
    ) -> List[int]:

        n = len(s)


        tree = [None] * (4 * n)

        def merge(left, right, left_len, right_len):
            lp, ls, lm, lc, lr = left
            rp, rs, rm, rc, rr = right

            prefix = lp
            if lp == left_len and lr == rc:
                prefix += rp

            suffix = rs
            if rs == right_len and lr == rc:
                suffix += ls

            maximum = max(lm, rm)

            if lr == rc:
                maximum = max(maximum, ls + rp)

            return (prefix, suffix, maximum, lc, rr)

        def build(i, l, r):
            if l == r:
                tree[i] = (1, 1, 1, s[l], s[l])
                return

            mid = (l + r) // 2

            build(2 * i + 1, l, mid)
            build(2 * i + 2, mid + 1, r)

            tree[i] = merge(
                tree[2 * i + 1],
                tree[2 * i + 2],
                mid - l + 1,
                r - mid
            )

        def update(i, l, r, pos, ch):
            if l == r:
                tree[i] = (1, 1, 1, ch, ch)
                return

            mid = (l + r) // 2

            if pos <= mid:
                update(2 * i + 1, l, mid, pos, ch)
            else:
                update(2 * i + 2, mid + 1, r, pos, ch)

            tree[i] = merge(
                tree[2 * i + 1],
                tree[2 * i + 2],
                mid - l + 1,
                r - mid
            )

        build(0, 0, n - 1)

        ans = []

        for ch, pos in zip(queryCharacters, queryIndices):
            update(0, 0, n - 1, pos, ch)
            ans.append(tree[0][2])

        return ans