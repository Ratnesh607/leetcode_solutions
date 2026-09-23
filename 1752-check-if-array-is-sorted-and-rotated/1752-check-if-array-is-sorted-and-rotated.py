class Solution:
    def check(self, nums: list[int]) -> bool:
        n = len(nums)
        start = -1
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                start = i + 1
                
        if start == -1:
            return True
        
        for i in range(start + 1, n + start ):
            if nums[i%n - 1] > nums[(i%n)]:
                return False
        return True