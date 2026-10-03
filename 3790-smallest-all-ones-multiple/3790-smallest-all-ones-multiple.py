class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        if k % 2 == 0:
            return -1

        n = 0
        for i in range(k):
            n *= 10
            n += 1
            n %= k
            if n == 0:
                return i + 1

        return -1
        