class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        sufMin = [0]* n
        sufMin[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            sufMin[i] = min(nums[i], sufMin[i + 1])

        preMax = 0
        for i in range(n):
            preMax = max(preMax, nums[i])
            if preMax - sufMin[i] <= k:
                return i
        return -1