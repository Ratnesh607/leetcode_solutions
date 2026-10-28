class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[False] * 1024 for _ in range(n)]
        dp[0][grid[0][0]] = True
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                prev = dp[j]
                left = dp[j - 1] if j > 0 else None
                curr = [False] * 1024
                for xorVal in range(1024):
                    if prev[xorVal]:
                        curr[xorVal ^ grid[i][j]] = True

                    if left is not None and left[xorVal]:
                        curr[xorVal ^ grid[i][j]] = True

                dp[j] = curr
        for xorVal in range(1024):
            if dp[n - 1][xorVal]:
                return xorVal

        return -1