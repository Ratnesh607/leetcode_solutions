class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) 
        count = 0
        for j in range(n):
            prev = grid[0][j]
            for i in range(1, m):
                if grid[i][j] <= prev:
                    count += prev - grid[i][j] + 1
                    prev += 1
                else:
                    prev = grid[i][j]

        return count