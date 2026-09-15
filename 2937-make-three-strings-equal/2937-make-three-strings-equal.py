class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        n = min(len(s1), len(s2), len(s3))
        i = 0
        while i < n:
            if s1[i] != s2[i] or s2[i] != s3[i]:
                break
            i += 1

        if i == 0:
            return -1
        return len(s1) + len(s2) + len(s3) - (3*i)
        