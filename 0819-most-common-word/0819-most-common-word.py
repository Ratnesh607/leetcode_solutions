class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        freq = {}
        word = []
        for i in paragraph:
            if "A" <= i <= "Z":
                word.append(chr(ord(i) - ord("A") + ord("a")))
            elif "a" <= i <= "z":
                word.append(i)

            elif word:
                word = "".join(word)
                freq[word] = freq.get(word, 0) + 1
                word = []

        if word:
            word = "".join(word)
            freq[word] = freq.get(word, 0) + 1

        for word in banned:
            if word in freq:
                del freq[word]

        maxFreq = max(freq.values())
        for i in freq:
            if freq[i] == maxFreq:
                return i
        