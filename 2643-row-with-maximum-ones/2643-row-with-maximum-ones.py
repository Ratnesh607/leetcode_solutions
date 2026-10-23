class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx = 0
        countMax = 0
        for i in range(len(mat)):
            countOne = sum(mat[i])
            if countMax < countOne:
                countMax = countOne
                idx = i

        return [idx, countMax]
        