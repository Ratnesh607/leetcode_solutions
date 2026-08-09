class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1
        while l < r and s[l] == s[r]:
            temp = s[l]
            while l <= r and s[l] == temp:
                l += 1

            while l <= r and s[r] == temp:
                r -= 1
        return max(0, r - l + 1)