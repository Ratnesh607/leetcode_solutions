class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        freq = [0]*10
        total = 0
        while n:
            digit = n % 10
            freq[digit] += 1
            factorial = 1
            while digit:
                factorial *= digit
                digit -= 1
            total += factorial
            n //= 10
        
        while total:
            freq[total % 10] -= 1
            total //= 10
        
        for i in freq:
            if i:
                return False
        return True