class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor = 0
        check_zero = False
        for i in nums:
            xor ^= i
            if i != 0:
                check_zero = True
        if xor:
            return n
        return n - 1 if check_zero else 0
        