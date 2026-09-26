class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        count = 0
        i = 0
        while i < len(s):
            if s[i] == "1":
                count = 0
                while i < len(s) and s[i] == "1":
                    count += 1
                    ans += count
                    i += 1
            i += 1
        return ans % (10**9 + 7)
        