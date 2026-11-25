class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        s = intervals[0][0]
        e = intervals[0][1]
        count = len(intervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] >= s and intervals[i][1] <= e:
                count -= 1
            else:
                s = intervals[i][0]
                e = intervals[i][1]

        return count