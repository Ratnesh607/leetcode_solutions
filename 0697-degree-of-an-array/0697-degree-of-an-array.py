class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        freq = {}
        first = {}
        last = {}
        for i in range(len(nums)):
            x = nums[i]
            freq[x] = freq.get(x, 0) + 1
            if x not in first:
                first[x] = i
            last[x] = i

        maxFreq = max(freq.values())
        shortest = len(nums)
        for i in freq:
            if freq[i] == maxFreq:
                shortest = min(shortest, last[i] - first[i] + 1)

        return shortest