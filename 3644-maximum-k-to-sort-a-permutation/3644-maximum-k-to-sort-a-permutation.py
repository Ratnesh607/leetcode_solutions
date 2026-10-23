class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            if nums[i] != i:
                ans &= nums[i]

        return ans if ans != -1 else 0
            
        