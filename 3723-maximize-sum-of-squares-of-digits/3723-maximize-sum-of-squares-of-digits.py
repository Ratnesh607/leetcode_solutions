class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum <= 9:
            return str(sum * 10**(num - 1))

        nine = sum // 9
        last = sum % 9

        if nine > num or (nine == num and last != 0):
            return ""

        ans = []
        for i in range(nine):
            ans.append("9")
            num -= 1
            if num == 0 and last == 0:
                return "".join(ans)
            if num == 0:
                return ""

        ans.append(str(last))
        num -= 1

        while num:
            ans.append("0")
            num -= 1

        return "".join(ans)
        