class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        x = 1

        for i in range(1, n):
            x *= i

        for i in range(1, k + 1):
            x *= i

        y = 1
        for i in range(n + k - 1, 0, -1):
            y *= i

        return (y // x) % 1000000007

        