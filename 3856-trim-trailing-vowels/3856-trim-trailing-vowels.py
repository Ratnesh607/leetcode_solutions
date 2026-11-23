class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        s = list(s)
        vowels = {"a", "e", "i", "o", "u"}
        i = len(s) - 1
        while i >= 0 and s[i] in vowels:
            s.pop()
            i -= 1
            
        return "".join(s)