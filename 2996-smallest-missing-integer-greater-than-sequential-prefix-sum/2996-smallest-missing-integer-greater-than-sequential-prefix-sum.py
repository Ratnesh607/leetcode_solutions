class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        arr = [False]*52
        for i in nums:
            arr[i] = True
        
        i = 1
        total = nums[0]
        while i < len(nums) and nums[i] == (nums[i - 1] + 1):
            total += nums[i]
            i += 1
        
        if total > 50:
            return total

        while arr[total]:
            total += 1
        return total