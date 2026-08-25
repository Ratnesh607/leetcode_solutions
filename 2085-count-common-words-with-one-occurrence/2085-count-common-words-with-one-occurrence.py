class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        freq1 = {}
        for i in words1:
            freq1[i] = freq1.get(i, 0)+1

        freq2 = {}
        for i in words2:
            freq2[i] = freq2.get(i, 0)+1
        
        count = 0
        for i in words1:
            if i in freq2 and freq1[i] == 1 and freq2[i] == 1:
                count += 1
        return count