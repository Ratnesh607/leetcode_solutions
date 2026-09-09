class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            digit = nums[i]
            digitSum = 0
            while digit:
                digitSum += digit % 10
                digit //= 10
            if digitSum == i:
                return i
        return -1
                