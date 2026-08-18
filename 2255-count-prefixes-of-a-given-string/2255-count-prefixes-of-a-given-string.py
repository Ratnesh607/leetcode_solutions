class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for i in words:
            if len(i) > len(s):
                continue
            j = 0
            while j < len(i) and i[j] == s[j]:
                j += 1
            if j == len(i):
                count += 1
        return count
        