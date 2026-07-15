class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        heap = []
        for i in freq:
            heapq.heappush(heap,[freq[i], i])
            if len(heap) > k:
                heapq.heappop(heap)
        return [i[1] for i in heap]