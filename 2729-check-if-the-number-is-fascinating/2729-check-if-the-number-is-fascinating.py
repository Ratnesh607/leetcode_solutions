class Solution:
    def isFascinating(self, n: int) -> bool:
        check = [False]*9
        temp = n
        for i in range(2,4):
            if temp * i >= 1000:
                n *= 10
            n *= 1000
            n += temp * i
        while n:
            if n % 10:
                if check[(n % 10) - 1]:
                    return False
                check[(n % 10) - 1] = True
            n //= 10
        for i in check:
            if not i:
                return False
        return True