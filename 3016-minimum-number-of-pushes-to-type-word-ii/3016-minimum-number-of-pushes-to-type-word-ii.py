class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = [0]*26
        for i in word:
            freq[ord(i) - ord("a")] += 1

        freq.sort(reverse=True)

        count = 0
        for i in range(26):
            if freq[i] == 0:
                break
            count += freq[i] * (i // 8 + 1)
        return count