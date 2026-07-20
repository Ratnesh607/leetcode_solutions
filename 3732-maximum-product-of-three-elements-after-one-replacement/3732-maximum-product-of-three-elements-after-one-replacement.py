class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largest1 = largest2 = float("-inf")
        smallest1 = smallest2 = float("inf")

        for i in nums:
            if largest1 < i:
                largest2, largest1 = largest1, i
            elif largest2 < i:
                largest2 = i
            
            if smallest1 > i:
                smallest2, smallest1 = smallest1, i
            elif smallest2 > i:
                smallest2 = i

        return max(largest1 * largest2 * 100000,
                   smallest1 * smallest2 * 100000 ,
                   largest1 * smallest1 * -100000)
        