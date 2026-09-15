class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upperFreq = [0]*26
        lowerFreq = [0]*26
        for i in word:
            if ord("A") <= ord(i) <= ord("Z"):
                upperFreq[ord(i) - ord("A")] = 1
            else:
                lowerFreq[ord(i) - ord("a")] = 1
        
        count = 0
        for i in range(26):
            if upperFreq[i] and lowerFreq[i]:
                count += 1

        return count