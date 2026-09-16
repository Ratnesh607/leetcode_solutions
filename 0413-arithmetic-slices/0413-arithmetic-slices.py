class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        ans = 0
        i = 0
        while i < len(nums) - 2:
            count = 0
            if nums[i] - nums[i + 1] == nums[i + 1] - nums[i + 2]:
                while i < len(nums) - 2 and nums[i] - nums[i + 1] == nums[i + 1] - nums[i + 2]:
                    i += 1
                    count += 1
                    ans += count
            i += 1
        return ans