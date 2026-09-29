class Solution:
    def sortSentence(self, s: str) -> str:
        spaces = 1
        for i in s:
            if i == " ":
                spaces += 1

        ans = [""]*spaces
        word = []
        for i in s:
            if i == " ":
                continue
            if ord("1") <= ord(i) <= ord("9"):
                word = "".join(word)
                ans[int(i) - 1] = word
                word = []
            else:
                word.append(i)
            
        return " ".join(ans)