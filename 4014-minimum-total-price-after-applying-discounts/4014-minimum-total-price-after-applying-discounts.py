class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        n = min(len(prices), len(discounts))
        prices.sort(reverse = True)
        discounts.sort(reverse = True)
        ans = 0
        for i in range(n):
            ans += prices[i] * (100 - discounts[i]) / 100

        for i in range(n, len(prices)):
            ans += prices[i]
            
        return ans