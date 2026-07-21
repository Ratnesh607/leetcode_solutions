class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        largest1 = largest2 = 0
        smallest1 = smallest2 = float("inf")

        for i in nums:
            if i >= largest1:
                largest2, largest1 = largest1, i
            elif i > largest2:
                largest2 = i

            if i <= smallest1:
                smallest2, smallest1 = smallest1, i
            elif i < smallest2:
                smallest2 = i

        return (largest1 * largest2) - (smallest1 * smallest2)
