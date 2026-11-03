class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d = 0
        for i in instructions:
            if i == "G":
                x += directions[d][0]
                y += directions[d][1]

            elif i == "R":
                d = (d + 1) % 4

            else:
                d = (d - 1) % 4

        return (x == 0 and y == 0) or d != 0
        