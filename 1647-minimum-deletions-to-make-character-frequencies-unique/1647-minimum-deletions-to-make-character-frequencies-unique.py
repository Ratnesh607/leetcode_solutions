class Solution:
    def minDeletions(self, s: str) -> int:
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1

        unique = {}
        count = 0
        for i in freq:
            if freq[i] not in unique:
                unique[freq[i]] = i
            else:
                for j in range(freq[i], 0, -1):
                    if freq[i] not in unique:
                        unique[freq[i]] = i
                        break
                    freq[i] -= 1
                    count += 1

        return count