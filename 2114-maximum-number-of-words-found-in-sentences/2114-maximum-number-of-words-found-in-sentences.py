class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sentence in sentences:
            countSpace = 0
            for i in sentence:
                if i == " ":
                    countSpace += 1

            ans = max(ans, countSpace + 1)
        return ans