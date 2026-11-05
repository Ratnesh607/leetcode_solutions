
class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        vals = sorted(set(nums))
        m = len(vals)
        ranks = {}
        for i in range(m):
            ranks[vals[i]] = i + 1

        count = [0] * (m + 1)
        sums = [0] * (m + 1)

        def update(tree, idx, val):
            while idx <= m:
                tree[idx] += val
                idx += idx & -idx

        def query(tree, idx):
            result = 0
            while idx > 0:
                result += tree[idx]
                idx -= idx & -idx
            return result

        def findKth(kth):
            idx = 0
            bit = 1 << (m.bit_length() - 1)

            while bit:
                nxt = idx + bit
                if nxt <= m and count[nxt] < kth:
                    idx = nxt
                    kth -= count[nxt]

                bit >>= 1

            return idx + 1

        costs = []
        total = 0
        for i in range(n):
            val = nums[i]
            idx = ranks[val]
            update(count, idx, 1)
            update(sums, idx, val)
            total += val
            if i >= x:
                old = nums[i - x]
                old_idx = ranks[old]
                update(count, old_idx, -1)
                update(sums, old_idx, -old)
                total -= old

            if i < x - 1:
                continue

            mid_idx = findKth((x + 1) // 2)
            median = vals[mid_idx - 1]
            left_count = query(count, mid_idx - 1)
            left_sum = query(sums, mid_idx - 1)
            cost = (median * left_count - left_sum)
            cost += (total - left_sum) - median * (x - left_count)
            costs.append(cost)

        prev = [0] * (n + 1)
        for j in range(1, k + 1):
            curr = [float('inf')] * (n + 1)

            for i in range(1, n + 1):
                curr[i] = curr[i - 1]
                if i >= x:
                    take = prev[i - x] + costs[i - x]
                    curr[i] = min(curr[i], take)

            prev = curr
        return prev[n]
