class Solution:
    def sortString(self, s: str) -> str:
        freq = [0]*26
        for i in s:
            freq[ord(i) - ord("a")] += 1

        result = []
        n = len(s)
        while n:
            for i in range(26):
                if freq[i]:
                    result.append(chr(i + ord("a")))
                    freq[i] -= 1
                    n -= 1
                    if not n:
                        return "".join(result)
            for i in range(25,-1,-1):
                if freq[i]:
                    result.append(chr(i + ord("a")))
                    freq[i] -= 1
                    n -= 1
                    if not n:
                        return "".join(result)
        return "".join(result)