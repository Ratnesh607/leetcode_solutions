class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        count = 0
        for i in s:
            if not count:
                count += 1
                continue
            if i == ")" and count == 1:
                count = 0
                close = 0
                continue

            ans.append(i)
            if i == "(":
                count += 1
            else:
                count -= 1

        return "".join(ans)