class Solution:
    def isIdealPermutation(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            if abs(nums[i] - i) > 1:
                return False
        return True