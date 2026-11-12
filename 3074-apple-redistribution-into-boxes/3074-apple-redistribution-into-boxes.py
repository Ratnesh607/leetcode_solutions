class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        total = sum(apple)
        cap = 0
        for i in range(len(capacity)):
            cap += capacity[i]
            if cap >= total:
                return i + 1

        return len(capacity)
