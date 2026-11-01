class Solution:
    def minimumFlips(self, n: int) -> int:
        binary = []
        while n > 0:
            rem = n % 2
            binary.append(rem)
            n //= 2

        count = 0
        left = 0
        right = len(binary) - 1
        while left < right:
            if binary[left] != binary[right]:
                count += 2
            left += 1
            right -= 1

        return count    