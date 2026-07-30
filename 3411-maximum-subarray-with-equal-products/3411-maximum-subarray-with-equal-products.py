class Solution:
    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            g = 0
            l = 1
            prod = 1
            for j in range(i, n):
                g = gcd(g, nums[j])
                l = lcm(l, nums[j])
                prod *= nums[j]

                if prod == g * l:
                    ans = max(ans, j - i + 1)
        return ans