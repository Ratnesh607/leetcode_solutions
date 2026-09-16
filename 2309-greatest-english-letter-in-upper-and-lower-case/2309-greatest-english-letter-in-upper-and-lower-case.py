class Solution:
    def greatestLetter(self, s: str) -> str:
        upperFreq = [False]*26
        lowerFreq = [False]*26
        for i in s:
            if ord("A") <= ord(i) <= ord("Z"):
                upperFreq[ord(i) - ord("A")] = True
            else:
                lowerFreq[ord(i) - ord("a")] = True
 
        for i in range(25,-1,-1):
            if upperFreq[i] and lowerFreq[i]:
                return chr(ord("A") + i)

        return ""