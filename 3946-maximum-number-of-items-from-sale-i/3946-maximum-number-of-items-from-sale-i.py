class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free = [0] * n
        min_price = float('inf')
        for i in range(n):
            min_price = min(min_price, items[i][1])
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        dp = [0] * (budget + 1)
        for i in range(n):
            price = items[i][1]
            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + free[i] + 1)

        ans = 0
        for i in range(budget + 1):
            ans = max(ans, dp[i] + (budget - i) // min_price)

        return ans
