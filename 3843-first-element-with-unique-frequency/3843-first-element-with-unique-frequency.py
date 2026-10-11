class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        freq_of_freq = {}
        for i in freq:
            freq_of_freq[freq[i]] = freq_of_freq.get(freq[i], 0) + 1

        idx = -1
        for i in freq_of_freq:
            if freq_of_freq[i] == 1:
                idx = i
                break

        for i in freq:
            if freq[i] == idx:
                return i

        return -1
        