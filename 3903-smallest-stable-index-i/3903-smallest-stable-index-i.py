class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        preMin = [0]* n
        preMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            preMin[i] = min(nums[i], preMin[i + 1])

        preMax = 0
        for i in range(n):
            preMax = max(preMax, nums[i])
            if preMax - preMin[i] <= k:
                return i
        return -1