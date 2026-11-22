class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = 0
        temp = n
        while temp:
            r *= 10
            r += temp % 10
            temp //= 10

        num = min(n, r)
        rev = max(n, r)
        ans = 0
        for i in range(num, rev + 1):
            if i == 1:
                continue
            flag = True
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    flag = False
                    break

            if flag:
                ans += i

        return ans