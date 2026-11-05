class Solution:
    def minRotations(self, s: str) -> int:
        count = 0
        prev = 0
        for i in range(len(s)):
            a = int(s[i])
            diff = abs(prev - a)
            count += min(diff, 10 - diff)
            prev = a

        return count
        