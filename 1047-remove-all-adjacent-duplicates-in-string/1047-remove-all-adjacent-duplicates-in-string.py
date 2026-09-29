class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans = []
        for i in range(len(s)):
            if not ans:
                ans.append(s[i])
                continue
            if s[i] == ans[-1]:
                ans.pop()
            else:
                ans.append(s[i])
        return "".join(ans)
            