class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        heapq.heapify(nums)
        count = 0
        x = heapq.heappop(nums)
        while x < k:            
            y = heapq.heappop(nums) 
            heapq.heappush(nums, (x*2) + y)
            x = heapq.heappop(nums)
            count += 1
            
        return count