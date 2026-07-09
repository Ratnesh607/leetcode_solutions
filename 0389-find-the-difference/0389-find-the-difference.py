class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        for i in t:
            if i in freq:
                freq[i] -= 1
                if freq[i] == 0:
                    del freq[i]
            else:
                return i
        
        return ""