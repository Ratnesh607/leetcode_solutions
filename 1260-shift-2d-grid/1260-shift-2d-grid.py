class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        row = len(grid)
        col = len(grid[0])
        n = row * col
        k %= n
        if k == 0:
            return grid

        def reverse(i: int, j: int) -> None:
            while i < j:
                    row1, col1 = i // col, i % col
                    row2, col2 = j // col, j % col
                    grid[row1][col1], grid[row2][col2] = grid[row2][col2], grid[row1][col1]

                    i += 1
                    j -= 1
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)

        return grid

        