class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustedBy = [0] * (n + 1)
        trusts = [0] * (n + 1)

        for i in trust:
            trusts[i[0]] += 1
            trustedBy[i[1]] += 1

        for i in range(1, n + 1):
            if trustedBy[i] == n - 1 and trusts[i] == 0:
                return i

        return -1