class Solution:
    def equalFrequency(self, word: str) -> bool:
        freq = [0] * 26
        for i in word:
            freq[ord(i) - ord("a")] += 1

        highest = max(freq)
        lowest = float("inf")
        distinct = 0
        for i in freq:
            if i:
                distinct += 1
                lowest = min(lowest, i)

        if distinct == 1:
            return True
            
        cHighest = 0
        cLowest = 0

        for i in freq:
            if i == highest:
                cHighest += 1
            elif i == lowest:
                cLowest += 1
            elif i != 0:
                return False

        if highest == lowest:
            return highest == 1

        if highest == lowest + 1 and cHighest == 1:
            return True

        if lowest == 1 and cLowest == 1:
            return True

        return False