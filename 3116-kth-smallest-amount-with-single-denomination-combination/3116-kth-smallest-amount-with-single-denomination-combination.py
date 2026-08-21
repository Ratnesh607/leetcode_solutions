class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def count(mid):
            def dfs(index, lcm, chosen):
                if index == len(coins):
                    if chosen == 0:
                        return 0

                    value = mid // lcm
                    return value if chosen % 2 else -value

                total = dfs(index + 1, lcm, chosen)
                new_lcm = math.lcm(lcm, coins[index])
                if new_lcm <= mid:
                    total += dfs(index + 1, new_lcm, chosen + 1)

                return total

            return dfs(0, 1, 0)

        left = 1
        right = max(coins) * k
        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left