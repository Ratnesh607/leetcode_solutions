class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        ans = []
        for i in words:
            word = i.lower()
            if word[0] in "qwertyuiop":
                row = "qwertyuiop"
            elif word[0] in "asdfghjkl":
                row = "asdfghjkl"
            elif word[0] in "zxcvbnm":
                row = "zxcvbnm"

            flag = True
            for j in word:
                if j not in row:
                    flag = False
                    break
            if flag:
                ans.append(i)
        return ans