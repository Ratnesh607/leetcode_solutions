class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        n = len(nums)
        total = sum(nums)
        target = total - x
        if target < 0:
            return -1

        if target == 0:
            return n

        i = 0
        currSum = 0
        maxLen = -1
        for j in range(n):
            currSum += nums[j]
            while i <= j and currSum > target:
                currSum -= nums[i]
                i += 1
            if currSum == target:
                maxLen = max(maxLen, j - i + 1)

        if maxLen == -1:
            return -1
        return n - maxLen