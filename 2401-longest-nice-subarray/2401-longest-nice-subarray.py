class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = 0
        ans = 0
        win = 0

        for r in range(len(nums)):
            while win & nums[r]:
                win ^= nums[l]
                l += 1

            win |= nums[r]
            ans = max(ans, r - l + 1)

        return ans