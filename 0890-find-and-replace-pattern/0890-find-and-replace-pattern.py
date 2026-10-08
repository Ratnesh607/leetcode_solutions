class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        m = len(words)
        n = len(words[0])
        ans = []
        for i in range(m):
            dict1 = {}
            dict2 = {}
            for j in range(n):
                if words[i][j] not in dict1:
                    dict1[words[i][j]] = pattern[j]

                if pattern[j] not in dict2:
                    dict2[pattern[j]] = words[i][j]

                if dict2[pattern[j]] != words[i][j] or dict1[words[i][j]] != pattern[j]:
                    break

                if j == n - 1:
                    ans.append(words[i])
                
        return ans


        