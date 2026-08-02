class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        preMax = [nums[0]]
        suffixMax = [nums[-1]]*n
        for i in range(1, n):
            preMax.append(max(nums[i], preMax[-1]))

        for i in range(n - 2, -1, -1):
            suffixMax[i] = max(suffixMax[i + 1], nums[i])
        
        ans = 0
        for i in range(n):
            if i - k >= 0:
                ans = max(ans, nums[i] + preMax[i - k])
            if i + k < n:
                ans = max(ans, nums[i] + suffixMax[i + k])

        return ans