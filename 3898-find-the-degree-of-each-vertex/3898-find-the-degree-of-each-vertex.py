class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        for i in range(len(matrix)):
            matrix[i] = sum(matrix[i])
        return matrix