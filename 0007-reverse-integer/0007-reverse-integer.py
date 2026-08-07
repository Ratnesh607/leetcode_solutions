class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x != abs(x):
            sign = -1
        temp = abs(x)
        ans = 0
        while temp:
            ans *= 10
            ans += temp % 10
            temp //= 10
        ans *= sign
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        return ans
        