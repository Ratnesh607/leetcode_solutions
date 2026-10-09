class Solution:
    def longestWord(self, words: list[str]) -> str:
        Set = set(words)
        ans = ""
        for i in words:
            valid = True
            for j in range(1, len(i) + 1):
                if i[:j] not in Set:
                    valid = False
                    break

            if valid:
                if len(i) > len(ans):
                    ans = i
                elif len(i) == len(ans) and i < ans:
                    ans = i
        return ans