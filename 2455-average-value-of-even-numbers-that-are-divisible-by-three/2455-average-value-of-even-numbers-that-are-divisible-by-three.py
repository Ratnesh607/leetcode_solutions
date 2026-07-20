class Solution:
    def averageValue(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for i in nums:
            if i % 6 == 0:
                total += i
                count += 1

        return total // count if count else 0