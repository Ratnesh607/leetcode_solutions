class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums):
            count = 0
            if nums[i] == 0:
                while i < len(nums) and nums[i] == 0:
                    i += 1
                    count += 1
                    ans += count
            i += 1
        return ans

        