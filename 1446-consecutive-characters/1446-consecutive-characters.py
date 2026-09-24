class Solution:
    def maxPower(self, s: str) -> int:
        char = ""
        count = 0
        ans = 0
        for i in s:
            if i == char:
                count += 1
            else:
                char = i
                count = 1
            ans = max(ans, count)
        return ans
        