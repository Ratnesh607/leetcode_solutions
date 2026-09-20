class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
        num = abs(x)
        ans = 0
        while num:
            ans *= 10
            ans += num % 10
            num //= 10
        ans *= sign
        return 0 if (ans < -2**31 or ans > 2**31 - 1) return ans
        
