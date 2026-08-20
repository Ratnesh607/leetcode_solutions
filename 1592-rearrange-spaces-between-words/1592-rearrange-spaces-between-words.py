class Solution:
    def reorderSpaces(self, text: str) -> str:
        n = len(text)
        space = 0
        words = 0
        status = False
        for i in text:
            if i != " " and status == False:
                status = True
                words += 1
            elif i == " ":
                status = False
                space += 1

        if words == 1:
            avgSpace = 0
            extra = space
        else:
            words -= 1
            avgSpace = space // words
            extra = space % words
        ans = []
        for i in range(n):
            if text[i] == " ":
                continue
            ans.append(text[i])
            if i != n - 1 and text[i + 1] == " " and words:
                for j in range(avgSpace):
                    ans.append(" ")
                words -= 1
        for i in range(extra):
            ans.append(" ")

        return "".join(ans)
            