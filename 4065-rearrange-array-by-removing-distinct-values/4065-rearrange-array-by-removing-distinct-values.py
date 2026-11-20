class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        max_el = max(nums) + 1
        freq = [0]*max_el
        for i in nums:
            freq[i] += 1

        ans = []
        while len(ans) != len(nums):
            for i in range(max_el):
                if freq[i]:
                    ans.append(i)
                    freq[i] -= 1
        return ans