class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        count = 0
        i = 1
        while n > 8:
            count += 8 * i
            i += 1
            n -= 8
        count += n * i
        return count
        