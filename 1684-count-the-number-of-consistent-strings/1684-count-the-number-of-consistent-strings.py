class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        freq = [0]*26
        for i in allowed:
            freq[ord(i) - ord("a")] = 1

        count = 0
        for word in words:
            n = len(word)
            for i in range(n):
                if not freq[ord(word[i]) - ord("a")]:
                    break
                if i == n - 1:
                    count += 1
        return count