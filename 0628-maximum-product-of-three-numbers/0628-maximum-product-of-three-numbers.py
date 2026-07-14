class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        largest1 = largest2 = largest3 = float("-inf")
        smallest1 = smallest2 = float("inf")

        for i in nums:
            if largest1 < i:
                largest3, largest2, largest1 = largest2, largest1, i
            elif largest2 < i:
                largest3, largest2 = largest2, i
            elif largest3 < i:
                largest3 = i

            if smallest1 > i:
                smallest2, smallest1 = smallest1, i
            elif smallest2 > i:
                smallest2 = i

        return max(largest1 * largest2 * largest3, smallest1 * smallest2 * largest1) 