class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        ans = [-1, -1]
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                ans[0] = abs(nums[i])
            else:
                nums[idx] *= -1

        for i in range(len(nums)):
            if nums[i] > 0:
                ans[1] = i + 1

        return ans