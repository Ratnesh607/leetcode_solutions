class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        idx = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
        last = [-1] * 5
        start = 0
        ans = 0
        for i in range(len(word)):
            if word[i] not in idx:
                start = i + 1
                last = [-1] * 5
                continue
            last[idx[word[i]]] = i
            if -1 not in last:
                ans += min(last) - start + 1

        return ans