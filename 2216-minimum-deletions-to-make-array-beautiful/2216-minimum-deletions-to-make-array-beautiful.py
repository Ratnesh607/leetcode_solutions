class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) - 1):
            if (i - count) % 2 == 0 and nums[i] == nums[i + 1]:
                count += 1

        if (len(nums) - count) % 2:
            count += 1

        return count