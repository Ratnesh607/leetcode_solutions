class Solution:
    def freqAlphabets(self, s: str) -> str:
        n = len(s)
        result = []
        i = 0
        while i < n:
            if i < n - 2 and s[i + 2] == "#":
                temp = int(s[i]) * 10 + int(s[i + 1]) - 1
                result.append(chr(ord("a") + temp))
                i += 3
            else:
                result.append(chr(ord("a") + int(s[i]) - 1))
                i += 1
        return "".join(result)