class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        countZero = 0
        countOne = 0
        zero = 0
        one = 0
        for i in s:
            if i == "1":
                countOne += 1
                countZero = 0
            else:
                countZero += 1
                countOne = 0
            zero = max(zero, countZero)
            one = max(one, countOne)
        return zero < one
                