class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 1
        count = 1
        for i in range(len(s) - 1):
            if ord(s[i]) + 1 == ord(s[i + 1]):
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        return ans