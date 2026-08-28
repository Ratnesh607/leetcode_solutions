class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        SecNum = {}
        for i in range(len(nums)):
            a = target-nums[i]
            if a in SecNum:
                return SecNum[a], i]
            SecNum[nums[i]] = i
