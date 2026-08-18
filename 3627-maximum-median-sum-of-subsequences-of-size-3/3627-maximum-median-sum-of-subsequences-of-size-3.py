class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        maxSum = 0
        while l < r - 1:
            maxSum += nums[r - 1]
            l += 1
            r -= 2
        return maxSum