class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])
        left = 0
        up = 1
        t = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                for cameFrom in range(2):
                    if row == m - 1 and col == n - 1:
                        t[row][col][cameFrom] = 1
                        continue
                    if grid[row][col] == 1:
                        if cameFrom == left:
                            t[row][col][cameFrom] = t[row + 1][col][up]
                        else:
                            t[row][col][cameFrom] = t[row][col + 1][left]
                        continue

                    total = 0
                    total += t[row][col + 1][left]
                    total += t[row + 1][col][up]
                    t[row][col][cameFrom] = total % MOD

        return t[0][0][left]    