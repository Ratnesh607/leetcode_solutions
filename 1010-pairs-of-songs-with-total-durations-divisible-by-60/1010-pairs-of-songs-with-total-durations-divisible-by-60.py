class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        rem = {}
        count = 0
        for i in time:
            temp = i % 60
            if temp in rem:
                count += rem[temp]

            temp = 60 - temp
            if temp == 60:
                temp = 0
            rem[temp] = rem.get(temp, 0) + 1

        return count
        