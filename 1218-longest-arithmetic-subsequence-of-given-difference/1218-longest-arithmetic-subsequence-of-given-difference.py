class Solution:
    def longestSubsequence(self, arr: list[int], difference: int) -> int:
        freq = {}
        ans = 0
        for i in arr:
            freq[i] = freq.get(i - difference, 0) + 1
            ans = max(ans, freq[i])
        return ans
        