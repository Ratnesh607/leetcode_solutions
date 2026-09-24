class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        count = 0
        ans = 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                count = 0
            ans = max(ans, count)
        return ans
        