class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc = 1
        dec = 1
        j = 0
        k = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                inc = max(inc, i - j)
                j = i

            if nums[i] >= nums[i - 1]:
                dec = max(dec, i - k)
                k = i
            if i == len(nums) - 1:
                inc = max(inc, i - j + 1)
                dec = max(dec, i - k + 1)
            
        return max(inc, dec)
        