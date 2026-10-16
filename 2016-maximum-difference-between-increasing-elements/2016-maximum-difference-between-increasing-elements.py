class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        minEl = nums[0]
        ans = -1
        for i in nums:
            minEl = min(minEl, i)
            if minEl < i:
                ans = max(ans, i - minEl)
        return ans