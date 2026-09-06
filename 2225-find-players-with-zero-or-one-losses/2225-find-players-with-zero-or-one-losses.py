class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        for i in range(len(matches)):
            if matches[i][0] not in losses:
                losses[matches[i][0]] = 0

            if matches[i][1] not in losses:
                losses[matches[i][1]] = 1
            else:
                losses[matches[i][1]] += 1

        ans1 = []
        ans2 = []
        for i in losses:
            if losses[i] == 0:
                ans1.append(i)
            elif losses[i] == 1:
                ans2.append(i)

        return [sorted(ans1), sorted(ans2)]