class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        result = [0] * k
        dp = [0] * k
        for num in nums:
            newDp = [0] * k
            rem = num % k
            newDp[rem] += 1
            for i in range(k):
                if dp[i]:
                    newRem = (i * rem) % k
                    newDp[newRem] += dp[i]

            for i in range(k):
                result[i] += newDp[i]
            dp = newDp

        return result