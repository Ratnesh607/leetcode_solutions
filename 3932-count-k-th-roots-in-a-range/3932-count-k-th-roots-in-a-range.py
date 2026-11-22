class Solution:
    def countKthRoots(self, l: int, r: int, k: int) -> int:
        if k == 1:
            return r - l + 1

        ans = 0
        for i in range(r + 1):
            num = i ** k
            if num > r:
                break

            if l <= num <= r:
                ans += 1

        return ans