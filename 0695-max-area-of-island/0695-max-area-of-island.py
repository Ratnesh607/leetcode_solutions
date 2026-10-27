class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        def bfs(grid,sr, sc):
            count = 1 
            m = len(grid)
            n = len(grid[0])
            queue = deque([(sr, sc)])
            directions = [(1,0),(-1, 0), (0,1), (0,-1)]
            grid[sr][sc] = 0

            while queue:
                r , c = queue.popleft()
                for i in directions:
                    nr = r + i[0]
                    nc = c + i[1]

                    if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                        count += 1
                        grid[nr][nc] = 0
                        queue.append((nr,nc))

            return count

        maxIsland = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    maxIsland = max(maxIsland, bfs(grid, i, j))

        return maxIsland
        