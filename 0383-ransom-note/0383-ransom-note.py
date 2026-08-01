class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        freq = {}
        for i in ransomNote:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in magazine:
            if (i in freq):
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]
        return not freq