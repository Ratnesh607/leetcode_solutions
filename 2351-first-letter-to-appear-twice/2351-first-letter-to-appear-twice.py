class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = [0]*26
        for i in s:
            freq[ord(i) - ord("a")] += 1
            if freq[ord(i) - ord("a")] > 1:
                return i        