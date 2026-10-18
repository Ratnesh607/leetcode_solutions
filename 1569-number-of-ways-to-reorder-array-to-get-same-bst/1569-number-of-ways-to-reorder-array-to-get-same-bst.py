class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        PT = [[1] * (i + 1) for i in range(n + 1)]
        for i in range(2, n + 1):
            for j in range(1, i):
                PT[i][j] = (PT[i - 1][j - 1] + PT[i - 1][j]) % mod

        def solve(nums):
            m = len(nums)
            if m < 3:
                return 1
            root = nums[0]
            l = []
            r = []
            for i in range(1, m):
                if nums[i] < root:
                    l.append(nums[i])
                else:
                    r.append(nums[i])

            lways = solve(l)
            rways = solve(r)
            return (lways * rways * PT[m - 1][len(l)]) % mod
        return (solve(nums) - 1) % mod
        