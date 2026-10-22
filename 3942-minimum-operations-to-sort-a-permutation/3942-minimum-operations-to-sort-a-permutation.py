class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        asc = True
        dsc = True
        for i in range(1, n):
            if nums[i] != (nums[i - 1] + 1) % n:
                asc = False
            if nums[i] != (nums[i - 1] - 1) % n:
                dsc = False

        ans = float('inf')
        if asc:
            ans = min(ans, zero, n - zero + 2)
        if dsc:
            ans = min(ans, zero + 2, n - zero)
        return -1 if ans == float('inf') else ans