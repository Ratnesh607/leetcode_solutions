class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest1 = largest2 = 0
        for i in nums:
            if largest1 < i:
                largest2, largest1 = largest1, i
            elif largest2 < i:
                largest2 = i
        return (largest1 - 1) * (largest2 - 1)
            