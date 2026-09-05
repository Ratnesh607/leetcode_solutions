class Solution:
    def similarPairs(self, words: List[str]) -> int:
        wordFreq = {}
        count = 0
        for word in words:
            letter = [False] * 26
            for i in word:
                letter[ord(i) - ord("a")] = True

            temp = []
            for i in range(26):
                if letter[i]:
                    temp.append(chr(i + ord("a")))

            temp = "".join(temp)
            if temp in wordFreq:
                count += wordFreq[temp]
            
            wordFreq[temp] = wordFreq.get(temp, 0) + 1

        return count

            