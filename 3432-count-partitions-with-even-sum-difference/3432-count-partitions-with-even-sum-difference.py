class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        Sum = 0
        count = 0
        for i in range(len(nums) - 1):
            Sum += nums[i]
            total -= nums[i]
            if (Sum - total) % 2 == 0:
                count += 1
        return count