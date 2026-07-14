class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        letters = {}
        k = 0
        for i in key:
            if i == " ":
                continue
            if i not in letters:
                letters[i] = chr(ord("a") + k)
                k += 1
            if k == 26:
                break

        ans = []
        for i in message:
            if i == " ":
                ans.append(i)
                continue
            ans.append(letters[i])
        return "".join(ans)
        