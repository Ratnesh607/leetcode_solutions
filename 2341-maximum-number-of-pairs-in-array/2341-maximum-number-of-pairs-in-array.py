class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = {}
        count = 0
        for i in nums:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
            if freq[i] == 2:
                del freq[i]
                count += 1
        return [count, len(nums) - (count * 2)]