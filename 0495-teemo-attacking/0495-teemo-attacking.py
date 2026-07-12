class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total_seconds = 0
        n = len(timeSeries)
        for i in range(n - 1):
            total_seconds += min(duration, timeSeries[i + 1] - timeSeries[i])
        return total_seconds + duration