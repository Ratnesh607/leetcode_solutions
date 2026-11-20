class Solution:
    def findMatrix(self, nums: list[int]) -> list[list[int]]:
        freq = {}
        max_freq = 0
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            max_freq = max(max_freq, freq[i])

        ans = [[] for _ in range(max_freq)]
        for i in freq:
            for j in range(freq[i]):
                ans[j].append(i)

        return ans
            