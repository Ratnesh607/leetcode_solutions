class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        cell = [0, 0]
        m = len(grid)
        n = len(grid[0])
        while True:
            i = cell[0]
            j = cell[1]
            curr = grid[i][j]
            grid[i][j] = "T"
            if curr == "R":
                j += 1
            elif curr == "L":
                j -= 1
            elif curr == "U":
                i -= 1
            else:
                i += 1

            if i < 0 or i >= m or j < 0 or j >= n:
                return cell
            if grid[i][j] == "T":
                return cell
                
            cell = [i, j]
