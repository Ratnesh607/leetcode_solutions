class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        min_el = float('inf')
        for i in range(n):
            total += nums[i]
            min_el = min(min_el, nums[i])

        return total - n * min_el