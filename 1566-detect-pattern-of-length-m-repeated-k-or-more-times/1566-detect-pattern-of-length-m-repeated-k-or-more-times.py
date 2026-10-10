class Solution:
    def containsPattern(self, arr: list[int], m: int, k: int) -> bool:
        count = 0
        for i in range(len(arr) - m):
            if arr[i] == arr[i + m]:
                count += 1
            else:
                count = 0

            if count == (k - 1) * m:
                return True
        return False
        