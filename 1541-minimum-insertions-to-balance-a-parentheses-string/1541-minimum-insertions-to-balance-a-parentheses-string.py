class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        result = 0
        count = 0
        i = 0
        while i < n:
            if s[i] == "(":
                count += 1
            else:
                if count > 0:
                    count -= 1
                else:
                    result += 1

                if i + 1 < n and s[i + 1] == ")":
                    i += 1

                else:
                    result += 1
            i += 1

        return result + count * 2