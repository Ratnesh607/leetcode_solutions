class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ans = 0
        prev = 0
        for i in brackets:
            temp = min(income, i[0] - prev)
            ans += temp * i[1] * 0.01
            income -= temp

            if income == 0:
                return ans
            prev = i[0]
        return ans