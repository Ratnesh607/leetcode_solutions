class Solution:
    def countSegments(self, s: str) -> int:
        if not s:
            return 0
        count = 0
        i = 0
        while i < len(s):
            if s[i] != " ":
                count += 1
                while i < len(s) and s[i] != " ":
                    i += 1
            else:
                i += 1

        return count
        