class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == " ":
                if i == 0:
                    ans.append(s[j - 1::-1])
                else:
                    ans.append(" ")
                    ans.append(s[j - 1:i - 1:-1])
                i = j + 1
            j += 1

        if i == 0:
            ans.append(s[j - 1::-1])
        else:
            ans.append(" ")
            ans.append(s[j - 1:i - 1:-1])

        return "".join(ans)