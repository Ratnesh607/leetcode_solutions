class Solution:
    def minMoves(self, nums: List[int]) -> int:
        MaxEl = max(nums)
        ans = 0
        for i in nums:
            ans += MaxEl - i
        return ans
