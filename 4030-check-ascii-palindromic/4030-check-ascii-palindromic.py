class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary = []
        for i in s:
            ascii = ord(i)
            for j in range(7, -1, -1):
                bit = (ascii >> j) & 1
                binary.append(bit)

        i = 0
        j = len(binary) - 1
        while i < j:
            if binary[i] != binary[j]:
                return False
            i += 1
            j -= 1

        return True
        