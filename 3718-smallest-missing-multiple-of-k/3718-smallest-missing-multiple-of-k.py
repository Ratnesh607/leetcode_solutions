class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        i = 1
        while i*k in nums:
            i += 1
        return i*k