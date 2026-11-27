class Solution:
    def countDominantElements(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1

        count = 0
        if nums[0] >= nums[1]:
            count += 1

        for i in range(1, len(nums) - 1):
            if (nums[i - 1] + nums[i + 1]) / 2 <= nums[i]:
                count += 1

        if nums[-1] >= nums[-2]:
            count += 1

        return count
        