class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i in range(len(piles)):
            piles[i] *= -1

        heapq.heapify(piles)
        
        while k:
            heapq.heappush(piles, heapq.heappop(piles) // 2)
            k -= 1

        return -sum(piles)