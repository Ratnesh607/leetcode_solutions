class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for i in range(1, n//2 + 1):
            a = i
            b = n - i
            while a:
                if a % 10 == 0:
                    break
                a //= 10
            if a == 0:
                while b:
                    if b % 10 == 0:
                        break
                    b //= 10

            if a == 0 and b == 0:
                return [i, n - i]       