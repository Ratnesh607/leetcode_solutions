class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l = 0
        r = 0
        a = 0
        b = float("inf")
        count = 0
        while r < len(s):
            if s[r] == "1":
                count += 1
                while count == k:
                    if b - a > r - l or (b - a == r - l and s[a:b + 1] > s[l : r + 1]):
                        a = l
                        b = r
                    if s[l] == "1":
                        count -= 1
                    l += 1
            r += 1

        return s[a:b+1] if b != float("inf") else ""
        