class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        freq = [0] * (n + 1)
        free = [0] * (n + 1)
        min_price = float('inf')
        for i in range(n):
            factor = items[i][0]
            price = items[i][1]
            freq[factor] += 1
            min_price = min(min_price, price)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                free[i] += freq[j]

            if freq[i] > 0:
                free[i] -= 1

        items.sort(key=lambda x: x[1])
        ans = 0
        for i in range(n):
            factor = items[i][0]
            price = items[i][1]
            if price > 2 * min_price:
                break

            count = min(free[factor], budget // price)
            ans += count * 2
            budget -= count * price

        ans += budget // min_price
        return ans
