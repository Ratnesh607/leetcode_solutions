class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        n = len(sentence)
        wordCount = 1
        i = 0
        j = 0
        while i < n:
            if sentence[i] == " ":
                wordCount += 1
                j = 0
                i += 1
                
            if sentence[i] == searchWord[j]:
                j += 1
                i += 1
                if j == len(searchWord):
                    return wordCount
                    
            else:
                while i < n and sentence[i] != " ":
                    i += 1

        return -1
            