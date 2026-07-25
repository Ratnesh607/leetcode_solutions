class Solution:
    def maxProduct(self, n: int) -> int:
        largest1 = largest2 = 0
        while n:
            temp = n % 10
            if largest1 <= temp:
                largest2, largest1 = largest1, temp
            elif largest2 < temp:
                largest2 = temp
            n //= 10
        return largest1 * largest2