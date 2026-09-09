class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        numsAvg = sum(nums) / len(nums)
        high = max(nums)
        start = int(numsAvg) + 1
        if start <= 0:
            start = 1

        if high < start:
            return start

        present = [False] * (high - start + 1)
        for i in nums:
            if start <= i <= high:
                present[i - start] = True

        for i in range(high - start + 1):
            if not present[i]:
                return start + i

        return high + 1