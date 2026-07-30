class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        freq = {}
        count = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                p = nums[i] * nums[j]
                count += freq.get(p, 0) * 8
                freq[p] = freq.get(p, 0) + 1
        return count

        