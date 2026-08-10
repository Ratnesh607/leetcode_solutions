class Solution:
    def baseNeg2(self, n: int) -> str:
        if n == 0:
            return "0"
        ans = []
        while n:
            rem = n % 2
            ans.append(str(rem))
            n = (n - rem) // -2

        return "".join(reversed(ans))
        
        