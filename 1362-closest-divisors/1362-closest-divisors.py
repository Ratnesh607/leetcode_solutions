class Solution:
    def closestDivisors(self, num: int) -> list[int]:
        n = int(num ** 0.5) + 1
        while True:
            if (num + 1) % n == 0:
                return [min(n, (num + 1) // n), max(n, (num + 1) // n)]
            if (num + 2) % n == 0:
                return [min(n, (num + 2) // n), max(n, (num + 2) // n)]

            n -= 1
        