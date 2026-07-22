class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        right = 0
        for i in range(len(nums) - 1, -1, -1):
            total -= nums[i]
            nums[i], right = abs(total - right), right + nums[i]
        return nums