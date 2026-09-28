class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        n = len(arr)
        heap = arr.copy()
        heapq.heapify(heap)
        count = 1
        idx = {}
        for i in range(n):
            temp = heapq.heappop(heap)
            if temp not in idx:
                idx[temp] = count
                count += 1

        ans = []
        for i in arr:
            ans.append(idx[i])
            
        return ans
        