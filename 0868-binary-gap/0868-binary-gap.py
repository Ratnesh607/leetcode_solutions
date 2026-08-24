class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        pos = 1
        prev = -1
        while n > 0:
            if n % 2:
                if prev != -1:
                    ans = max(ans, pos - prev)
                prev = pos
            pos += 1
            n //= 2
        return ans
