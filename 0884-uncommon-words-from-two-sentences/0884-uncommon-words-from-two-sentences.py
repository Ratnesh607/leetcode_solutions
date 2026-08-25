class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        check = {}
        l = 0
        for i in range(len(s1)):
            if s1[i] == " ":
                check[s1[l:i]] = check.get(s1[l:i], 0) + 1
                l = i + 1
            if i == len(s1) - 1:
                check[s1[l:i + 1]] = check.get(s1[l:i + 1], 0) + 1
        l = 0
        for i in range(len(s2)):
            if s2[i] == " ":
                check[s2[l:i]] = check.get(s2[l:i], 0) + 1
                l = i + 1
            if i == len(s2) - 1:
                check[s2[l:i + 1]] = check.get(s2[l:i + 1], 0) + 1

        ans = []
        for i in check:
            if check[i] == 1:
                ans.append(i)
        return ans