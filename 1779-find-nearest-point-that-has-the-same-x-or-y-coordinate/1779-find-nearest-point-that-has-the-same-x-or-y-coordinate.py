class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        prev = float("inf")
        index = -1
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                temp = abs(points[i][0] - x) + abs(points[i][1] - y)
                if temp < prev:
                    prev = temp
                    index = i
        return index        