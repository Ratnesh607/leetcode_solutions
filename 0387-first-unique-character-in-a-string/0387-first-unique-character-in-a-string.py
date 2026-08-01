class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = [0]*26
        for i in s:
            freq[ord(i) - ord("a")] += 1
        for i in range(len(s)):
            if freq[ord(s[i]) - ord("a")] == 1:
                return i
        return -1