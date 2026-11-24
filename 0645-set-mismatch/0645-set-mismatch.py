class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [-1, -1]
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1
            if freq[i] == 2:
                ans[0] = i
        for i in range(1, n + 1):
            if i not in freq:
                ans[1] = i
                return ans