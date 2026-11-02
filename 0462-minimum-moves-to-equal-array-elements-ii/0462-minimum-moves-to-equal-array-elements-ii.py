class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid = len(nums) // 2
        target = nums[mid]
        count = 0
        for i in range(len(nums)):
            count += abs(nums[i] - target)

        return count