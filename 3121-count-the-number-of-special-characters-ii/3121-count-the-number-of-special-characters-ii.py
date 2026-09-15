class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        upperFreq = [float("inf")]*26
        lowerFreq = [-1]*26
        for i in range(len(word)):
            if ord("A") <= ord(word[i]) <= ord("Z"):
                upperFreq[ord(word[i]) - ord("A")] = min(upperFreq[ord(word[i]) - ord("A")], i)
            else:
                lowerFreq[ord(word[i]) - ord("a")] = max(lowerFreq[ord(word[i]) - ord("a")], i)
        
        count = 0
        for i in range(26):
            if upperFreq[i] != float("inf") and lowerFreq[i] != -1 and lowerFreq[i] < upperFreq[i]:
                count += 1

        return count
        