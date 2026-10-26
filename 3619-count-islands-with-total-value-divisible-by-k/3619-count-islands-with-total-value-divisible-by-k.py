class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                stack = [(i, j)]
                total = grid[i][j]
                grid[i][j] = 0
                while stack:
                    x, y = stack.pop()

                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nx = x + dx
                        ny = y + dy
                        if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] > 0:
                            total += grid[nx][ny]
                            stack.append((nx, ny))
                            grid[nx][ny] = 0

                if total % k == 0:
                    count += 1
        return count
