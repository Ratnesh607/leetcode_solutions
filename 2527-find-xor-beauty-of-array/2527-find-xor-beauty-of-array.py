class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        xor = 0
        for i in nums:
            xor = xor ^ i
        return xor
        