class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        lKnownSum = 0
        rKnownSum = 0
        lQnCount = 0
        rQnCount = 0
        for i in range(n):
            if num[i] == '?':
                if i < n // 2:
                    lQnCount += 1
                else:
                    rQnCount += 1
            else:
                if i < n // 2:
                    lKnownSum += int(num[i])
                else:
                    rKnownSum += int(num[i])

        totalQnMarks = lQnCount + rQnCount
        if totalQnMarks % 2 == 1:
            return True

        LEFT = 2 * lKnownSum + 9 * lQnCount
        RIGHT = 2 * rKnownSum + 9 * rQnCount
        if LEFT == RIGHT:
            return False
        return True