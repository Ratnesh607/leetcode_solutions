class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        a, b, c = float('inf'), float('inf'), 0
        for i in range(1, n + 1):
            curr = costs[i-1] + min(a + 9, b + 4, c + 1)
            a = b
            b = c
            c = curr

        return c