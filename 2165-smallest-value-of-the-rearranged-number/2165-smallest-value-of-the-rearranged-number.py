class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0

        digits = []
        zeeros = []

        temp = abs(num)
        while temp:
            if temp % 10:
                digits.append(temp % 10)
            else:
                zeeros.append(temp % 10)
            temp //= 10

        ans = 0
        if num < 0:
            digits.sort(reverse = True)
            for i in digits:
                ans *= 10
                ans += i
            for i in zeeros:
                ans *= 10
            return -1 * ans

        digits.sort()
        ans = digits[0]
        for i in zeeros:
            ans *= 10
        for i in range(1, len(digits)):
            ans *= 10
            ans += digits[i]
        return ans