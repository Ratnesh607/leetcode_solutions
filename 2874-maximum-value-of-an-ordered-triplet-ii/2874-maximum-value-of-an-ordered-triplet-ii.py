class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i = nums[0]
        max_diff = 0
        ans = 0
        for i in range(1, len(nums)):
            ans = max(ans, max_diff * nums[i])
            max_diff = max(max_diff, max_i - nums[i])
            max_i = max(max_i, nums[i])
        return ans