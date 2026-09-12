class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        for i in range(n):
            intervals[i].append(i)
        intervals.sort()
        nextIdx = [n] * n
        for i in range(n):
            lo = i + 1
            hi = n - 1
            result = n
            while lo <= hi:
                mid = (lo + hi) // 2
                if intervals[mid][0] > intervals[i][1]:
                    result = mid
                    hi = mid - 1
                else:
                    lo = mid + 1

            nextIdx[i] = result

        dp = [[None] * 5 for _ in range(n + 1)]
        def solve(i, k):
            if k == 0 or i >= n:
                return (0, [])
            if dp[i][k] is not None:
                return dp[i][k]
            skipScore, skipIdx = solve(i + 1, k)
            takeScore, takeIdx = solve(nextIdx[i], k - 1)
            takeScore += intervals[i][2]
            takeIdx = takeIdx.copy()
            takeIdx.append(intervals[i][3])
            takeIdx.sort()
            if skipScore > takeScore:
                result = (skipScore, skipIdx)

            elif skipScore < takeScore:
                result = (takeScore, takeIdx)

            else:
                if skipIdx < takeIdx:
                    result = (skipScore, skipIdx)
                else:
                    result = (takeScore, takeIdx)
            dp[i][k] = result
            return result
        return solve(0, 4)[1]