class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        startH = int(startTime[0]) * 10 + int(startTime[1])
        startM = int(startTime[3]) * 10 + int(startTime[4])

        startS = int(startTime[6]) * 10 + int(startTime[7])

        endH = int(endTime[0]) * 10 + int(endTime[1])

        endM = int(endTime[3]) * 10 + int(endTime[4])

        endS = int(endTime[6]) * 10 + int(endTime[7])

        if endS < startS:
            endS += 60
            endM -= 1
        if endM < startM:
            endM += 60
            endH -= 1

        return (endH - startH) * 3600 + (endM - startM) * 60 + (endS - startS)
        