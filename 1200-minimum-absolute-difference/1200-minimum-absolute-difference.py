class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        arr.sort()
        ans = []
        minDiff = float("inf")
        for i in range(len(arr) - 1):
            minDiff = min(minDiff, abs(arr[i] - arr[i + 1]))

        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == minDiff:
                ans.append([arr[i], arr[i + 1]]) 
            
        return ans
        