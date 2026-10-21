class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        temp = 0
        minVal = 0
        for i in nums:
            temp += i
            minVal = min(minVal, temp)

        return 1 - minVal
        