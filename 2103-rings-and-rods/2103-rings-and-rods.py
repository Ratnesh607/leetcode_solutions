class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0
        roads = [""]*10
        for i in range(0,len(rings),2):
            if rings[i] not in roads[int(rings[i+1])]:
                roads[int(rings[i+1])] += rings[i]
        for i in range(0,10):
            if len(roads[i]) == 3:
                count += 1
        return count