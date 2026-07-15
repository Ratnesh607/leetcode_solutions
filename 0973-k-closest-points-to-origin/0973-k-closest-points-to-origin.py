class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            distance = points[i][0] ** 2 + points[i][1] ** 2

            heapq.heappush(heap, (-distance, i))
            if len(heap) > k:
                heapq.heappop(heap)

        return [points[i[1]] for i in heap]
        