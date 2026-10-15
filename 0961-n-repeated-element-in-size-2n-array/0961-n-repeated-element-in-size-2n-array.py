class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        unique = set()
        for i in nums:
            if i in unique:
                return i
            unique.add(i)