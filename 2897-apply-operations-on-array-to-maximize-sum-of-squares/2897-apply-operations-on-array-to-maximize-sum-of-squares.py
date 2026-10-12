class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        bitCount = [0]*32
        for i in nums:
            for b in range(32):
                if i & (1 << b):
                    bitCount[b] += 1

        result = 0
        while k:
            temp = 0
            for b in range(32):
                if bitCount[b]:
                    bitCount[b] -= 1
                    temp |=  1 << b

            result += temp * temp
            k -= 1

        return result % (10**9 + 7)

        