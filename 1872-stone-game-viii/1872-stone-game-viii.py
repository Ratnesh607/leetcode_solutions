class Solution:
    def stoneGameVIII(self, stones: list[int]) -> int:
        n = len(stones)
        prefixSums = [0] * n
        prefixSums[0] = stones[0]
        for i in range(1, n):
            prefixSums[i] = prefixSums[i - 1] + stones[i]

        ans = prefixSums[-1]
        for i in range(n - 2, 0, -1):
            ans = max(ans, prefixSums[i] - ans)

        return ans