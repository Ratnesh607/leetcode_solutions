class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while k:
            heapq.heapreplace(nums, nums[0] + 1)
            k -= 1

        product = 1
        MOD = 10**9 + 7
        for i in nums:
            product *= i
            product %= MOD
        return product