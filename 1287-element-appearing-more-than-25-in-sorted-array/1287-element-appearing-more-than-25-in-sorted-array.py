class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        j = n // 4
        for i in range(n - j):
            if arr[i] == arr[i + j]:
                return arr[i]
        