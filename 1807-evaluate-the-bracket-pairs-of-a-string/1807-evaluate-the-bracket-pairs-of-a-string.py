class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        n = len(s)
        Dict = {}
        for i in knowledge:
            Dict[i[0]] = i[1]
        
        i = 0
        ans = []
        while i < n:
            if s[i] == "(":
                i += 1
                word = []
                while s[i] != ")":
                    word.append(s[i])
                    i += 1
                word = "".join(word)
                
                if word in Dict:
                    ans.append(Dict[word])
                else:
                    ans.append("?")
            else:
                ans.append(s[i])
            i += 1

        return "".join(ans)
        