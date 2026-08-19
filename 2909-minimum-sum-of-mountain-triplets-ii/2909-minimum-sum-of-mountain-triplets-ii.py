class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        n = len(nums)
        suffix = [0] * n
        suffix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = min(suffix[i + 1], nums[i])

        ans = float("inf")
        preMin = nums[0]

        for i in range(n):
            preMin = min(preMin, nums[i])
            if preMin < nums[i] and suffix[i] < nums[i]:
                ans = min(ans, preMin + suffix[i] + nums[i])

        return ans if ans != float("inf") else -1
