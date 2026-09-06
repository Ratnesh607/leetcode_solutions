class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        total = 0
        for i in nums:
            total += i
        nums.sort(reverse=True)
        Sum = 0
        for i in range(len(nums)):
            Sum += nums[i]
            if Sum > (total - Sum):
                return nums[0 : i + 1]
