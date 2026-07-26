class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)
        ans = []
        for i in range(len(s)):
            char = (ord(s[i]) - ord('a') + total) % 26
            ans.append(chr(char + ord('a')))
            total -= shifts[i]
        return "".join(ans)
        