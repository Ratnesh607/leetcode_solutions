class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        if i == 0:
            return False

        temp = i
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1

        if i == temp:
            return False
            
        temp = i
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        if i == temp:
            return False

        return i == n - 1