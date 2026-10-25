class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        for num in range(left, right + 1):
            covered = False
            for i in ranges:
                if i[0] <= num <= i[1]:
                    covered = True
                    break
            if not covered:
                return False
        return True
        