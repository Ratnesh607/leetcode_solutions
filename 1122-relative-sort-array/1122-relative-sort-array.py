class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq = {}
        for i in arr1:
            freq[i] = freq.get(i, 0)+1

        ans = []
        for i in arr2:
            while freq[i]:
                ans.append(i)
                freq[i] -= 1
            del freq[i]

        if not freq:
            return ans

        heap = []
        for i in freq:
            heapq.heappush(heap, i)

        while heap:
            i = heapq.heappop(heap)
            while freq[i]:
                ans.append(i)
                freq[i] -= 1
            del freq[i]

        return ans