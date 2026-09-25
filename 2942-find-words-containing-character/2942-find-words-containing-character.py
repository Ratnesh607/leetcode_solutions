class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for i in range(len(words)):
            for j in words[i]:
                if j == x:
                    indices.append(i)
                    break
        return indices