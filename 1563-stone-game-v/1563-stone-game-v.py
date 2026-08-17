class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @lru_cache(None)
        def dp(l, r):
            if l == r:
                return 0

            ans = 0
            left_sum = 0
            right_sum = prefix[r + 1] - prefix[l]
            for mid in range(l, r):
                left_sum += stoneValue[mid]
                right_sum -= stoneValue[mid]

                if left_sum < right_sum:
                    if 2 * left_sum <= ans:
                        continue

                    ans = max(
                        ans,
                        left_sum + dp(l, mid)
                    )

                elif left_sum > right_sum:
                    if 2 * right_sum <= ans:
                        break
                    ans = max(
                        ans,
                        right_sum + dp(mid + 1, r)
                    )

                else:
                    ans = max(
                        ans,
                        left_sum + dp(l, mid),
                        right_sum + dp(mid + 1, r)
                    )
            return ans
        return dp(0, n - 1)