class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if len(result) >= 2 and result[-1] == result[-2] == s[i]:
                continue
            result.append(s[i])

        return "".join(result)

        