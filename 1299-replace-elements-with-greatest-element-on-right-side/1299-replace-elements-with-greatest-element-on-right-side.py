class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        maxEl = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = maxEl
            maxEl = max(maxEl, curr)
        return arr