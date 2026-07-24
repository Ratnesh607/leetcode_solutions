class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        for i in range(len(nums)):
            nums[i] *= -1

        heapq.heapify(nums)
        total = 0

        while k:
            temp = -heapq.heappop(nums)
            total += temp
            heapq.heappush(nums, -math.ceil(temp / 3))
            k -= 1
            
        return total
        