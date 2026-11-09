class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        busy = []
        count = [0] * k
        tree = [0] * (4 * k)
        def build(node, left, right):
            if left == right:
                tree[node] = 1
                return

            mid = (left + right) // 2
            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)
            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def update(node, left, right, idx, val):
            if left == right:
                tree[node] = val
                return

            mid = (left + right) // 2
            if idx <= mid:
                update(node * 2, left, mid, idx, val)
            else:
                update(node * 2 + 1, mid + 1, right, idx, val)

            tree[node] = tree[node * 2] + tree[node * 2 + 1]

        def find(node, left, right, ql, qr):
            if right < ql or left > qr or tree[node] == 0:
                return -1

            if left == right:
                return left

            mid = (left + right) // 2
            res = find(node * 2, left, mid, ql, qr)
            if res != -1:
                return res

            return find(node * 2 + 1, mid + 1, right, ql, qr)
        build(1, 0, k - 1)
        for i in range(len(arrival)):
            while busy and busy[0][0] <= arrival[i]:
                time, idx = heapq.heappop(busy)
                update(1, 0, k - 1, idx, 1)

            start = i % k
            idx = find(1, 0, k - 1, start, k - 1)
            if idx == -1:
                idx = find(1, 0, k - 1, 0, start - 1)

            if idx == -1:
                continue

            count[idx] += 1
            update(1, 0, k - 1, idx, 0)
            heapq.heappush(busy, (arrival[i] + load[i], idx))
        maximum = max(count)
        return [i for i in range(k) if count[i] == maximum]