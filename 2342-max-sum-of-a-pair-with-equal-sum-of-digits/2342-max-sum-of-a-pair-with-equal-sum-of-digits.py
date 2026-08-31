class Solution:
    def digitSum(self, num: int) -> int:
        Sum = 0
        while num:
            Sum += num % 10
            num //= 10

        return Sum

    def maximumSum(self, nums: List[int]) -> int:
        ans = -1
        best = {}
        for i in nums:
            Sum = self.digitSum(i)
            if Sum not in best:
                best[Sum] = i
            else:
                ans = max(ans, best[Sum] + i)
                best[Sum] = max(best[Sum], i)

        return ans