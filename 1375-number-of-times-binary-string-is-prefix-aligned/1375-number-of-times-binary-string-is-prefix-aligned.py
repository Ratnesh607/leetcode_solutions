class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxBulb = -1
        BulbsTurnedOn = 0
        count = 0
        for i in range(len(flips)):
            maxBulb = max(maxBulb, flips[i])
            BulbsTurnedOn += 1
            if maxBulb == BulbsTurnedOn:
                count += 1

        return count
        