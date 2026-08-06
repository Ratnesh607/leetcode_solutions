class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        minRow = [min(row) for row in matrix]

        maxCol = [0] * n
        for j in range(n):
            maxCol[j] = max(matrix[i][j] for i in range(m))

        ans = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == minRow[i] == maxCol[j]:
                    ans.append(matrix[i][j])
        return ans