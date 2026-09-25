class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        less = 0
        equal = 0
        for i in nums:
            if i < target:
                less += 1
            elif i == target:
                equal += 1

        indices = [i for i in range(less, equal + less)]
        
        return indices
        