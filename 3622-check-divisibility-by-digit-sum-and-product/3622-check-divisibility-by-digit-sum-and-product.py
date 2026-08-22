class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digitSum = 0
        product = 1
        num = n
        while num:
            digit = num % 10
            digitSum += digit
            product *= digit
            num //= 10
        return n % (digitSum + product) == 0