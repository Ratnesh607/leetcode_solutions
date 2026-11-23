class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        freq = {}
        x = 101
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            x = min(x, i)

        y = 101
        for i in nums:
            if freq[i] != freq[x]:
                y = min(y, i)

        return [x, y] if y != 101 else [-1,-1]