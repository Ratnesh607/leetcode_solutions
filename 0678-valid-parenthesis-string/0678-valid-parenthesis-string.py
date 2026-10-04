class Solution:
    def checkValidString(self, s: str) -> bool:
        open = 0
        close = 0
        n = len(s)
        for i in range(n):
            if s[i] == "(" or s[i] == "*":
                open += 1
            else:
                open -= 1
            if open < 0:
                return False

        for i in range(n - 1, -1, -1):
            if s[i] == ")" or s[i] == "*":
                close += 1
            else:
                close -= 1
            if close < 0:
                return False
        return True