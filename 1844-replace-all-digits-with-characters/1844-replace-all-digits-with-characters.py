class Solution:
    def replaceDigits(self, s: str) -> str:
        result = list(s)
        for i in range(1, len(result), 2):
            result[i] = chr(ord(result[i - 1]) + int(result[i]))

        return "".join(result)