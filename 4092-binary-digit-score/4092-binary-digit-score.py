class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        s1 = 0
        while a > 0:
            rem = a % 2
            if rem:
                s1 += 1
            
            a //= 2

        s2 = 0
        while b > 0:
            rem = b % 2
            if rem:
                s2 += 1
            
            b //= 2
        
        if s1 >= s2:
            return s1 * s2
        return s2 // s1
        