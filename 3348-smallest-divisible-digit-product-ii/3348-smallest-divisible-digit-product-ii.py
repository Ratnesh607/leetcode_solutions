import math

class Solution:
    def freeSlotsFiller(self, required: int, length: int) -> str:
        res = []
        
        for digit in range(9, 1, -1):
            while required % digit == 0:
                res.append(str(digit))
                required //= digit
                
        while len(res) < length:
            res.append('1')
            
        res.reverse()
        return "".join(res)

    def smallestNumber(self, num: str, t: int) -> str:
        n = len(num)
        
        temp = t
        for primeFact in [2, 3, 5, 7]:
            while temp % primeFact == 0:
                temp //= primeFact
                
        if temp != 1:
            return "-1"
            
        remainingFactor = [t] * (n + 1)
        for i in range(n):
            digit = int(num[i])
            
            if digit == 0:
                break
                
            remainingFactor[i+1] = remainingFactor[i] // math.gcd(remainingFactor[i], digit)
            
        if remainingFactor[n] == 1:
            return num
            
        zeroPos = num.find('0')
        zeroIdx = n - 1
        if zeroPos != -1:
            zeroIdx = zeroPos
            
        for i in range(zeroIdx, -1, -1):
            required = remainingFactor[i]
            freeSlots = n - 1 - i
            
            for digit in range(int(num[i]) + 1, 10):
                furtherRequired = required // math.gcd(required, digit)
                requiredNumber = self.freeSlotsFiller(furtherRequired, freeSlots)
                
                if len(requiredNumber) == freeSlots:
                    return num[:i] + str(digit) + requiredNumber
                    
        return self.freeSlotsFiller(t, n + 1)