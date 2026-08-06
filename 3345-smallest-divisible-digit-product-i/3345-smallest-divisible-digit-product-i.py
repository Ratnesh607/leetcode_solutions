class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            temp = n
            product = 1
            while temp:
                product *= temp % 10
                if product % t == 0:
                    return n
                temp //= 10

            n += 1

        