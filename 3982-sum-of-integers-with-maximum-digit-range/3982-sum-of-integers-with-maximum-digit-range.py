class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        MaxDigitRange = 0
        ans = 0
        for i in nums:
            num = i
            maxDigit = 0
            minDigit = 9
            while num:
                digit = num % 10
                maxDigit = max(maxDigit, digit)
                minDigit = min(minDigit, digit)
                num //= 10
            if MaxDigitRange < maxDigit - minDigit:
                MaxDigitRange = maxDigit - minDigit
                ans = i
            elif MaxDigitRange == maxDigit - minDigit:
                ans += i
        return ans
        