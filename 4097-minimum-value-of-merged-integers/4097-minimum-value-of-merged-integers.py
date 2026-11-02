class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        ans = float("inf")
        for i in range(0, len(nums), 2):
            temp = nums[i + 1]
            count = 0
            while temp:
                count += 1
                temp //= 10

            ans = min(ans, (10**count * nums[i]) + nums[i + 1])
            
        return ans