class Solution:
    def canAliceWin(self, n: int) -> bool:
        count = 0
        stones = 10
        while n >= stones:
            n -= stones
            stones -= 1
            count += 1

        return count % 2 == 1