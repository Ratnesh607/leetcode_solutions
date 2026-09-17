class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        i = 0
        j = 0
        currSum = 0
        minBestLenTillIdx = [float("inf")] * n
        bestMinLen = float("inf")
        result = float("inf")
        while j < n:
            currSum += arr[j]
            while i < j and currSum > target:
                currSum -= arr[i]
                i += 1

            if currSum == target:
                length = j - i + 1
                if i > 0 and minBestLenTillIdx[i - 1] != float("inf"):
                    result = min(result, length + minBestLenTillIdx[i - 1])

                bestMinLen = min(bestMinLen, length)
            minBestLenTillIdx[j] = bestMinLen
            j += 1
        if result == float("inf"):
            return -1
        return result