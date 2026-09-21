class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        sign = 1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if not sign:
                    return False

                if i == 0 or nums[i - 1] <= nums[i + 1]:
                    nums[i] = nums[i + 1]
                else:
                    if i + 2 < len(nums) and nums[i] > nums[i + 2]:
                        return False
                    nums[i + 1] = nums[i]
                sign = 0

        return True