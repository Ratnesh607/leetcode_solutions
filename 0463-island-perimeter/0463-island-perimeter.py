class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:

        def bfs(grid, sr, sc):
            m = len(grid)
            n = len(grid[0])
            count = 0
            queue = deque([(sr, sc)])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            grid[sr][sc] = -1

            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        count += 1

                    elif grid[nr][nc] == 0:
                        count += 1

                    elif grid[nr][nc] == 1:
                        grid[nr][nc] = -1
                        queue.append((nr, nc))
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return bfs(grid, i, j)

        return 0    