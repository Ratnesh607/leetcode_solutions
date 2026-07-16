class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        mxi = float("-inf")
        for i in range(len(nums)):
            mxi = max(mxi, nums[i])
            nums[i] = gcd(nums[i], mxi)
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = 0
        while i < j:
            ans += gcd(nums[i], nums[j])
            i += 1
            j -= 1
        return ans