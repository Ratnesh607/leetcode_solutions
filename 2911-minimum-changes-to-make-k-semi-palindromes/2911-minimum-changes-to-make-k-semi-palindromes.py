class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[n] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                length = j - i + 1
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    cnt = 0
                    for x in range(d):
                        l = i + x
                        r = j - d + 1 + x
                        while l < r:
                            if s[l] != s[r]:
                                cnt += 1

                            l += d
                            r -= d
                    cost[i][j] = min(cost[i][j], cnt)

        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                for p in range(i - 1):
                    if i - p < 2:
                        continue

                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])

        return dp[n][k]
