class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = 0
        rightSum = sum(nums)
        count = 0
        for i in range(n - 1):
            leftSum += nums[i]
            rightSum -= nums[i]
            if leftSum >= rightSum:
                count += 1
        return count