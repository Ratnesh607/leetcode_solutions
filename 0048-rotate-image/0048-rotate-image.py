class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        for i in range(n):
            a = 0
            b = n - 1
            while a < b:
                matrix[i][a], matrix[i][b] = matrix[i][b], matrix[i][a]
                a += 1
                b -= 1
        
        """
        Do not return anything, modify matrix in-place instead.
        """
        