class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        freq = [0]*26
        for i in licensePlate:
            if ord("A") <= ord(i) <= ord("Z"):
                freq[ord(i) - ord("A")] += 1
            elif ord("a") <= ord(i) <= ord("z"):
                freq[ord(i) - ord("a")] += 1

        idx = -1
        minLen = float("inf")
        for i in range(len(words)):
            temp = [0]*26
            for j in words[i]:
                temp[ord(j) - ord("a")] += 1

            valid = True
            for j in range(26):
                if freq[j] > temp[j]:
                    valid = False
                    break

            if valid and len(words[i]) < minLen:
                minLen = len(words[i])
                idx = i

        return words[idx]