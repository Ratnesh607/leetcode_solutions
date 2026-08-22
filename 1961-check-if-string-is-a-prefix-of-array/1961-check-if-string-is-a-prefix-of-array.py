class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i = 0
        for j in words:
            temp = len(j)
            if s[i:i + temp] != j:
                return False
            i += temp
            if i >= len(s):
                return True
        return i >= len(s)
            
        