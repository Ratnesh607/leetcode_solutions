class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = abs(nums[i])
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = 0
        while i < j:
            ans += nums[j]**2
            ans -= nums[i]**2
            i += 1
            j -= 1

        if len(nums) % 2:
            ans += nums[j]**2

        return ans
        