class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp0 = 1
        dp1 = 1
        ans = 1
        prev = float('-inf')
        for i in nums:
            if i == prev:
                dp1 = dp0 + 1

            elif i == prev + 1:
                dp0 += 1
                dp1 += 1

            elif i == prev + 2:
                dp0 = dp1 + 1
                dp1 = 1

            else:
                dp0 = 1
                dp1 = 1

            ans = max(ans, dp0, dp1)
            prev = i

        return ans
            