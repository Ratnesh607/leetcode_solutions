class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = []
        n = num
        while n:
            digits.append(n % 10)
            n //= 10
        digits  = digits[::-1]
        
        nine = 9
        for i in digits:
            if i != 9:
                nine = i
                break

        zero = digits[0]

        maxNum = 0
        minNum = 0
        for i in digits:
            maxNum *= 10
            minNum *= 10
            if i == nine:
                maxNum += 9
            else:
                maxNum += i

            if i != zero:
                minNum += i

        return maxNum - minNum
        