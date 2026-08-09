class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def solve(i, M):
            if i >= n:
                return 0
            if 2 * M >= n - i:
                return suffix[i]

            ans = 0
            for x in range(1, 2 * M + 1):
                opponent = solve(i + x, max(M, x))
                ans = max(ans, suffix[i] - opponent)
            return ans
        return solve(0, 1)    