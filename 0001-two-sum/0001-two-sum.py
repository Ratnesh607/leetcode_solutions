class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Dict = {}
        for i in range(len(nums)):
            a = target-nums[i]
            if a in Dict:
                return [Dict[a], i]
            Dict[nums[i]] = i