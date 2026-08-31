class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = []
        temp = num
        while temp:
            digits.append(temp % 10)
            temp //= 10

        digits2 = sorted(digits)
        digit = -1
        digit2 = -1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != digits2[i]:
                digit = digits[i]
                digit2 = digits2[i]
                digits[i] = digits2[i]
                break

        for i in range(len(digits)):
            if digits[i] == digit2:
                digits[i] = digit
                break

        ans = 0
        for i in range(len(digits) - 1, -1, -1):
            ans *= 10
            ans += digits[i]
        return ans