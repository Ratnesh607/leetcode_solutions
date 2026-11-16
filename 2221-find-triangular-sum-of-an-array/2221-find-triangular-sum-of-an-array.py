class Solution:
    def triangularSum(self, nums: list[int]) -> int:
        while len(nums) != 1:
            total = []
            for i in range(len(nums) - 1):
                total.append((nums[i] + nums[i + 1])%10)

            nums = total

        return nums[0]