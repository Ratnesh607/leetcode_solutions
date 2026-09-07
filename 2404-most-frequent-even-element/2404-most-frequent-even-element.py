class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        ans = -1
        for i in nums:
            if i % 2:
                continue
            freq[i] = freq.get(i, 0) + 1
            if ans == -1:
                ans = i
            elif freq[i] > freq[ans]:
                ans = i
            elif freq[i] == freq[ans] and i < ans:
                ans = i

        return ans