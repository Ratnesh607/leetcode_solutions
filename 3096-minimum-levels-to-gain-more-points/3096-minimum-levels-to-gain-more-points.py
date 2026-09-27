class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        Bob = 0
        for i in possible:
            if i:
                Bob += 1
            else:
                Bob -= 1

        Alice = 0
        for i in range(len(possible) - 1):
            if possible[i]:
                Bob -= 1
                Alice += 1
            else:
                Bob += 1
                Alice -= 1
            if Alice > Bob:
                return i + 1
        return -1
            

        