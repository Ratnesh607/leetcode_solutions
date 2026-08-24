class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        binary = []
        while n > 0:
            rem = n % 2
            binary.append(rem)
            n //= 2

        i = 0
        while i < len(binary):
            if binary[i] == 1:
                temp = i
                i += 1
                while i < len(binary) and binary[i] != 1:
                    i += 1

                if i < len(binary):
                    ans = max(ans, i - temp)
                    i -= 1
            i += 1
        return ans