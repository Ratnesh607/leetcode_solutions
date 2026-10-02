class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        def solve(curr, open, close):
            if len(curr) == 2 * n:
                result.append(curr)
                return

            if open < n:
                solve(curr + "(", open + 1, close)
            if close < open:
                solve(curr + ")", open, close + 1)

        solve("", 0, 0)
        return result