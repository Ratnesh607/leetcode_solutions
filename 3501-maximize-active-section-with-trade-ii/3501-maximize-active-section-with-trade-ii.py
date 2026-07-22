class Solution:
    def build(self, i, left, right, st, arr):
        if left == right:
            st[i] = arr[left]
            return

        mid = (left + right) // 2
        self.build(2 * i + 1, left, mid, st, arr)
        self.build(2 * i + 2, mid + 1, right, st, arr)
        st[i] = max(st[2 * i + 1], st[2 * i + 2])

    def query(self, start, end, i, left, right, st):

        if left > end or right < start:
            return 0

        if start <= left and right <= end:
            return st[i]

        mid = (left + right) // 2
        return max(
            self.query(start, end, 2 * i + 1, left, mid, st),
            self.query(start, end, 2 * i + 2, mid + 1, right, st)
        )

    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:

        n = len(s)
        countActive = s.count("1")
        start = []
        end = []
        i = 0
        while i < n:
            if s[i] == "0":
                left = i
                while i < n and s[i] == "0":
                    i += 1

                start.append(left)
                end.append(i - 1)
            else:
                i += 1
        m = len(start)
        if m < 2:
            return [countActive] * len(queries)

        size = []
        for i in range(m):
            size.append(end[i] - start[i] + 1)

        pair = []
        for i in range(m - 1):
            pair.append(size[i] + size[i + 1])

        st = [0] * (4 * len(pair))
        self.build(0, 0, len(pair) - 1, st, pair)

        ans = []
        for left, right in queries:
            low = bisect_left(end, left)
            high = bisect_right(start, right) - 1
            gain = 0

            if low < high:
                first = end[low] - max(start[low], left) + 1
                last = min(end[high], right) - start[high] + 1
                if high - low == 1:
                    gain = first + last

                else:
                    a = first + size[low + 1]
                    b = size[high - 1] + last
                    c = 0
                    if low + 1 <= high - 2:
                        c = self.query(
                            low + 1,
                            high - 2,
                            0,
                            0,
                            len(pair) - 1,
                            st
                        )
                    gain = max(a, b, c)
            ans.append(countActive + gain)
        return ans