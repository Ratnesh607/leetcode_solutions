class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        rightSum = sum(nums)
        leftSum = 0
        index = -1
        minDiff = float("inf")
        for i in range(n):
            leftSum += nums[i]
            rightSum -= nums[i]
            a = leftSum // (i + 1)
            if i == n - 1:
                b = 0
            else:
                b = rightSum // (n - i - 1)
            if abs(a - b) < minDiff:
                minDiff = abs(a - b)
                index = i
        return index