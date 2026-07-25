class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if start > destination:
            start, destination = destination, start

        total1 = 0
        for i in range(start, destination):
            total1 += distance[i]

        total2 = 0
        i = start
        while i != destination:
            i = (i - 1) % len(distance)
            total2 += distance[i]

        return min(total1, total2)