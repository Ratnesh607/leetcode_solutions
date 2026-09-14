class Solution:
    def capitalizeTitle(self, title: str) -> str:
        word = []
        ans = []
        for i in range(len(title)):
            if title[i] != " " and i != len(title) - 1:
                word.append(title[i])
            else:
                if i == len(title) - 1:
                    word.append(title[i])

                n = len(word)
                if n <= 2:
                    for j in range(n):
                        if ord("A") <= ord(word[j]) <= ord("Z"):
                            word[j] = chr(ord(word[j]) - ord("A") + ord("a"))

                else:
                    if ord("a") <= ord(word[0]) <= ord("z"):
                        word[0] = chr(ord(word[0]) - ord("a") + ord("A"))

                    for j in range(1, n):
                        if ord("A") <= ord(word[j]) <= ord("Z"):
                            word[j] = chr(ord(word[j]) - ord("A") + ord("a"))
                word = "".join(word)
                ans.append(word)
                word = []
                
        return " ".join(ans)