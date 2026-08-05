class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        if max(nums) < 6:
            return 0
        total = 0
        for i in nums:
            if i < 6:
                continue
            count = 2
            temp = isqrt(i)
            Sum = 1 + i
            for j in range(2, temp+1):
                if i % j == 0:
                    count += 1
                    Sum += j
                    if j * j != i:
                        count += 1
                        Sum += i // j
            if count == 4:
                total += Sum

        return total
