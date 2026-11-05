class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        count = 0
        prev = 0
        for i in nums:
            if i != prev:
                prev = i
                count += 1
        return len(nums) - count