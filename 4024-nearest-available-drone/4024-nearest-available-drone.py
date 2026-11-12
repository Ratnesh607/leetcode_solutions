class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        idx = -1
        diff = float("inf")
        for i in range(len(drones)):
            r = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
            if r > drones[i][2]:
                continue
            
            if diff > r:
                idx = i
                diff = r

        return idx