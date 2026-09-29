class Solution:
    def findSubarrays(self, nums: list[int]) -> bool:
        Hash = set()
        for i in range(len(nums) - 1):
            Sum = nums[i] + nums[i + 1]
            if Sum in Hash:
                return True
            Hash.add(Sum)

        return False
        