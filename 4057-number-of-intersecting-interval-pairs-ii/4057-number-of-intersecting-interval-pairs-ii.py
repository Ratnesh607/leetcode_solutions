class Solution:
    def countIntersectingIntervals(self, intervals: list[list[int]]) -> int:
        temoravlin = intervals
        temoravlin.sort()
        heap = []
        count = 0
        for start, end in temoravlin:
            while heap and heap[0] < start:
                heapq.heappop(heap)

            count += len(heap)
            heapq.heappush(heap, end)

        return count