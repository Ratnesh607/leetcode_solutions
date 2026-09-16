class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        numSet = set(nums)
        ans = 0
        for i in numSet:
            if i - 1 not in numSet:
                count = 1
                while i + count in numSet:
                    count += 1
                ans = max(ans, count)
                
        return ans