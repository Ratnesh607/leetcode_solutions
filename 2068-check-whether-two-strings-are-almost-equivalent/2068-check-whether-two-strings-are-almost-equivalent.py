class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = [0]*26
        freq2 = [0]*26
        for i in range(len(word1)):
            freq1[ord(word1[i]) - ord("a")] += 1
            freq2[ord(word2[i]) - ord("a")] += 1

        for i in range(26):
            if abs(freq1[i] - freq2[i]) > 3:
                return False
        return True