class Solution:
    def checkValid(self, matrix: list[list[int]]) -> bool:
        n = len(matrix)
        target = (1 << n) - 1
        for i in range(n):
            row = 0
            col = 0
            for j in range(n):
                row |= 1 << (matrix[i][j] - 1)
                col |= 1 << (matrix[j][i] - 1)

            if row != target or col != target:
                return False

        return True