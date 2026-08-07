class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r = 0
        l = len(mat) - 1
        ans = 0
        for i in range(len(mat)):
            if r == l:
                ans += mat[i][r]
            else:
                ans += mat[i][r] + mat[i][l]
            r += 1
            l -= 1
        return ans
        