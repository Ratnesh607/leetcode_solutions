class Solution:
    def reverseDegree(self, s: str) -> int:
        Sum = 0
        for i in range(len(s)):
            posi = 26 - (ord(s[i]) - ord("a")) 
            product = posi * (i + 1)
            Sum += product
        return Sum
        