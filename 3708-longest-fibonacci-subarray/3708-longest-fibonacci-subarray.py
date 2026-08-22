class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = 2
        i = 0
        while i < (len(nums) - 2):
            start = i
            while i < len(nums) - 2 and nums[i] + nums[i + 1] == nums[i + 2]:
                i += 1
            ans = max(ans, i - start + 2)
            i += 1
        return ans