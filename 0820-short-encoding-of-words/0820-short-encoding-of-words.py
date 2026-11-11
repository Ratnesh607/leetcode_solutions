class Solution:
    def minimumLengthEncoding(self, words: list[str]) -> int:
        words = set(words)
        count = 0
        for word in list(words):
            for i in range(1, len(word)):
                words.discard(word[i:])

        for word in words:
            count += len(word) + 1
        return count