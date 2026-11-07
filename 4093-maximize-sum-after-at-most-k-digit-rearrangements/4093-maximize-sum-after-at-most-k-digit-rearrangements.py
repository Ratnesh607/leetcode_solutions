class Solution:
    def maximizeSum(self, nums: list[int], k: int) -> int:
        k_largest = []
        for i in nums:
            digits = []
            num = i
            while num:
                digits.append(num % 10)
                num //= 10
            digits.sort(reverse = True)
            num = 0
            for j in digits:
                num *= 10
                num += j

            diff = num - i
            heapq.heappush(k_largest, diff)
            if len(k_largest) > k:
                heapq.heappop(k_largest)

        return sum(k_largest) + sum(nums)

        