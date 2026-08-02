class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)

        suffix = 1
        for i in range(n - 1, -1, -1):
            total -= nums[i]
            if total == suffix:
                return i
            suffix *= nums[i]
            if suffix >= total:
                break

        return -1