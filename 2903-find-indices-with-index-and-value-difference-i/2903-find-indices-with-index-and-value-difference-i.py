class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        minValue = nums[0]
        maxValue = nums[0]
        minIndex = 0
        maxIndex = 0
        for j in range(indexDifference, n):
            i = j - indexDifference
            if nums[i] < minValue:
                minValue = nums[i]
                minIndex = i

            if nums[i] > maxValue:
                maxValue = nums[i]
                maxIndex = i

            if abs(nums[j] - minValue) >= valueDifference:
                return [minIndex, j]

            if abs(nums[j] - maxValue) >= valueDifference:
                return [maxIndex, j]

        return [-1, -1]