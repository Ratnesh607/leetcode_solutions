class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = [0] * 101
        for x in nums:
            freq[x] += 1

        ans = 0
        for i in range(1, 101):
            if freq[i] == 1:
                ans += i
        return ans  