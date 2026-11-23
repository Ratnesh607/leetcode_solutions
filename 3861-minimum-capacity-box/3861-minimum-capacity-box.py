class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        idx = -1
        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if idx == -1:
                    idx = i
                else:
                    if capacity[idx] > capacity[i]:
                        idx = i

        return idx
