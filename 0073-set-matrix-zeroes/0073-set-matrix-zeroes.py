class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])
        firstRow = False
        firstColumn = False
        for j in range(n):
            if matrix[0][j] == 0:
                firstRow = True

        for i in range(m):
            if matrix[i][0] == 0:
                firstColumn = True

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if firstRow:
            for j in range(n):
                matrix[0][j] = 0

        if firstColumn:
            for i in range(m):
                matrix[i][0] = 0