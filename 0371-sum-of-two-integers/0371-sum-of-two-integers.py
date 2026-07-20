class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 65535
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
    
        return a if a <= 32767 else ~(a ^ mask)
