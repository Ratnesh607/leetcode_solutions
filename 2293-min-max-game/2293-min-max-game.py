class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        while len(nums) > 2:
            total = []
            for i in range(0, len(nums) - 3,4):
                total.append(min(nums[i], nums[i + 1]))
                total.append(max(nums[i + 2], nums[i + 3]))

            nums = total
        return min(nums)