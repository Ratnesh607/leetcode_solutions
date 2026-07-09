class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        digit = [0]*10
        num1 = float("inf")
        num2 = float("inf")

        for i in nums1:
            digit[i] += 1
            num1 = min(num1, i)

        for i in nums2:
            digit[i] += 1
            num2 = min(num2, i)
            
        for i in range(10):
            if digit[i] == 2:
                return i
        
        return min(num1 * 10 + num2, num2 * 10 + num1)
        