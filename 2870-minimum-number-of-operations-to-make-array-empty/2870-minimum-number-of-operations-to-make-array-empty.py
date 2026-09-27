class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        count = 0
        for i in freq:
            if freq[i] == 1:
                return -1
            count += freq[i] // 3
            if freq[i] % 3 != 0:
                count += 1
                
        return count