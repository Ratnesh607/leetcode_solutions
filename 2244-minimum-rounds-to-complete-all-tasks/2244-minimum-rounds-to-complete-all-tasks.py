class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        freq = {}
        for i in tasks:
            freq[i] = freq.get(i, 0) + 1

        count = 0
        for i in freq:
            if freq[i] == 1:
                return -1
            count += freq[i] // 3
            if freq[i] % 3 != 0:
                count += 1
                
        return count