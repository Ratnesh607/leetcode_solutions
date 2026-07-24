class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:

        for i in range(len(gifts)):
            gifts[i] *= -1

        heapq.heapify(gifts)
        

        while k:
            temp = -heapq.heappop(gifts)
            heapq.heappush(gifts, -isqrt(temp))
            k -= 1
            
        return -sum(gifts)
        
        