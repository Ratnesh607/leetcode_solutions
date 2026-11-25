class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod1 = 10**9 + 7
        mod2 = 10**9 + 9
        base1 = 911382323
        base2 = 972663749

        p1 = [0]*(n+1)
        p2 = [0]*(n+1)
        pow1 = [1]*(n+1)
        pow2 = [1]*(n+1)

        for i in range(n):
            p1[i+1] = (p1[i]*base1 + nums[i]) % mod1
            p2[i+1] = (p2[i]*base2 + nums[i]) % mod2
            pow1[i+1] = (pow1[i]*base1) % mod1
            pow2[i+1] = (pow2[i]*base2) % mod2

        def check(k):
            freq = {}
            for i in range(n-k+1):
                h1 = (p1[i+k] - p1[i]*pow1[k]) % mod1
                h2 = (p2[i+k] - p2[i]*pow2[k]) % mod2
                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            for value in freq.values():
                if value == 1:
                    return True

            return False

        low = 1
        high = n
        ans = n
        while low <= high:
            mid = (low + high)//2
            if check(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
