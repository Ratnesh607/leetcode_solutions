class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        while i < len(s)-2:
            if s[i] == "a" and s[i+1] == "b" and s[i+2] == "c":
                s = s[:i] + s[i+3:]
                i = 0
            else:
                i += 1
        return not s
        