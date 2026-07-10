class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        count = 0
        for i in range(len(s)):
            if s[i] == "1" and (i == len(s) - 1 or s[i + 1] == "0"):
                count += 1
            if count > 1:
                return False
        return True
        