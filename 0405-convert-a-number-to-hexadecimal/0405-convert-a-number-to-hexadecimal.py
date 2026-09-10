class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hexDeci = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"]
        hexStr = []
        if num < 0:
            num = 4294967296 + num
        while num:
            hexStr.append(hexDeci[num % 16])
            num //= 16

        hexStr = hexStr[::-1] 
        return "".join(hexStr)