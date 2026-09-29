class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m = len(grid)
        n = len(grid[0])
        if (m + n - 1) % 2 == 1:
            return False

        dp = [[set() for _ in range(n)] for _ in range(m)]
        if grid[0][0] == "(":
            dp[0][0].add(1)

        for i in range(m):
            for j in range(n):
                for balance in dp[i][j]:
                    if i + 1 < m:
                        if grid[i + 1][j] == "(":
                            dp[i + 1][j].add(balance + 1)
                        elif balance > 0:
                            dp[i + 1][j].add(balance - 1)

                    if j + 1 < n:
                        if grid[i][j + 1] == "(":
                            dp[i][j + 1].add(balance + 1)
                        elif balance > 0:
                            dp[i][j + 1].add(balance - 1)

        return 0 in dp[m - 1][n - 1]