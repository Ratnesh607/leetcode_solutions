class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        specialSum = 0
        for i in range(1,int(isqrt(n))+1):
            if n % i == 0:
                specialSum += nums[i - 1]*nums[i - 1]
                if i*i != n:
                    specialSum += nums[(n // i) - 1] * nums[(n // i) - 1]
        return specialSum
        