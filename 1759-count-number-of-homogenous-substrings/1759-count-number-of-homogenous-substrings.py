class Solution:
    def countHomogenous(self, s: str) -> int:
        char = ""
        count = 0
        ans = 0
        for i in s:
            if i == char:
                count += 1
            else:
                char = i
                count = 1
            ans += count
        ans %= 10**9 + 7
        return ans
        