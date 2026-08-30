class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2:
            return n
            
        minEl = min(nums)
        maxEl = max(nums)
        minIdx = -1
        maxIdx = -1
        for i in range(n):
            if nums[i] == minEl:
                minIdx = i
            if nums[i] == maxEl:
                maxIdx = i

        if minIdx > maxIdx:
            minIdx, maxIdx = maxIdx, minIdx
        l = maxIdx + 1
        c = minIdx + 1 + (n - maxIdx)
        r = n - minIdx
        return min(l, c, r)