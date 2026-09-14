class Solution:
    def toLowerCase(self, s: str) -> str:
        ans = []
        for i in s:
            if ord("A") <= ord(i) <= ord("Z"):
                ans.append(chr(ord(i) - ord("A") + ord("a")))
            else:
                ans.append(i)
                
        return "".join(ans)
        