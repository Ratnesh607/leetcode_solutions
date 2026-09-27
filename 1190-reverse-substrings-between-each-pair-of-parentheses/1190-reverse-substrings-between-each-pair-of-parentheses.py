class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [-1] * n
        stack = []
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        ans = []
        i = 0
        direction = 1
        while i < n:
            if s[i] == "(" or s[i] == ")":
                i = pair[i]
                direction = -direction
            else:
                ans.append(s[i])
            i += direction
            
        return "".join(ans)