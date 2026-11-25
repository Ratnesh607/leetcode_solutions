class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        i = 0
        j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            if firstList[i][0] <= secondList[j][1] and firstList[i][1] >= secondList[j][0]:
                ans.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])

            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans
