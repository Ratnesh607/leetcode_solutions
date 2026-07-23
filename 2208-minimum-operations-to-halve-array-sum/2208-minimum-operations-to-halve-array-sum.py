class Solution:
    def halveArray(self, nums: List[int]) -> int:
        target = sum(nums) / 2
        for i in range(len(nums)):
            nums[i] *= -1

        heapq.heapify(nums)
        reuced = 0
        countOp = 0
        while reuced < target:
            temp = heapq.heappop(nums) / 2
            heapq.heappush(nums, temp)
            countOp += 1
            reuced += abs(temp)
        return countOp
        