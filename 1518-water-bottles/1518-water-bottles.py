class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        extra = 0
        count = numBottles
        while numBottles >= numExchange:
            extra = numBottles % numExchange
            numBottles //= numExchange
            count += numBottles
            numBottles += extra
        return count

        