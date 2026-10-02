class Solution:
    def entityParser(self, text: str) -> str:
        keywords = {"&quot;" : '"', "&apos;" : "'", "&amp;" : "&", "&gt;" : ">" , "&lt;" : "<", "&frasl;" : "/"} 
        ans = []
        word = ""
        for i in text:
            if i == " " and word:
                ans.append(word)
                ans.append(" ")
                word = ""
            else:
                if i == "&":
                    ans.append(word)
                    word = ""
                word += i

            if word in keywords:
                ans.append(keywords[word])
                word = ""

        if word:
            ans.append(word)

        return "".join(ans)