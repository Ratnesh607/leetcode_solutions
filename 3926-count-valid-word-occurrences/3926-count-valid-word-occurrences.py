class Solution:
    def countWordOccurrences(self, chunks: list[str], queries: list[str]) -> list[int]:
        s = "".join(chunks)
        freq = {}
        start = 0
        for i in range(len(s)):
            if s[i] == " ":
                if start < i:
                    word = s[start:i]
                    freq[word] = freq.get(word, 0) + 1
                start = i + 1

            elif s[i] == "-":
                if not (i > 0 and i < len(s) - 1 and "a" <= s[i - 1] <= "z" and "a" <= s[i + 1] <= "z"):
                    if start < i:
                        word = s[start:i]
                        freq[word] = freq.get(word, 0) + 1

                    start = i + 1

        if start < len(s):
            word = s[start:]
            freq[word] = freq.get(word, 0) + 1

        ans = []
        for word in queries:
            ans.append(freq.get(word, 0))

        return ans