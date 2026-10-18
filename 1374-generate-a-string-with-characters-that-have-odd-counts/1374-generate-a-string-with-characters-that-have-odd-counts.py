class Solution:
    def generateTheString(self, n: int) -> str:
        ans = []
        if n % 2 == 0:
            ans.append("a")
            n -= 1
        for i in range(n):
            ans.append("b")
        return "".join(ans)
        