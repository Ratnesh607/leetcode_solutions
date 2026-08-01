class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for i in nums:
            index = abs(i) - 1
            if nums[index] < 0:
                result.append(abs(i))
            else:
                nums[index] *= -1
        return result
        