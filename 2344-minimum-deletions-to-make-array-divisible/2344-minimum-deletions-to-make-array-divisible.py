class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        deletion = 0
        nums.sort()
        g = max(numsDivide)
        for i in numsDivide:
            g = gcd(i, g)
        for i in nums:
            if g % i == 0:
                return deletion
            deletion += 1
        return -1    