class Solution:
    def minimalKSum(self, nums: list[int], k: int) -> int:
        nums = sorted(set(nums))
        total = 0
        prev = 0
        for i in nums:
            count = i - prev - 1
            temp = min(count, k)
            total += temp * (2 * prev + temp + 1) // 2
            k -= temp
            prev = i
            if k == 0:
                return total

        total += k * (2 * prev + k + 1) // 2
        return total
