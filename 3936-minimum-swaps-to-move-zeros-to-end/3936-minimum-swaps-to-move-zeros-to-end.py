class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        zeros = 0
        for i in nums:
            if not i:
                zeros += 1

        ans = zeros
        for i in range(len(nums) - 1, len(nums) - zeros - 1, -1):
            if not nums[i]:
                ans -= 1

        return ans 