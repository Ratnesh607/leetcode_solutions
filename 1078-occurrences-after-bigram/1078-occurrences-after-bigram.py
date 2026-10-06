class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        s = []
        word = []
        for i in text:
            if i == " ":
                word = "".join(word)
                s.append(word)
                word = []
            else:
                word.append(i)
        word = "".join(word)
        s.append(word)

        ans = []
        for i in range(len(s) - 2):
            if s[i] == first and s[i + 1] == second:
                ans.append(s[i + 2])

        return ans