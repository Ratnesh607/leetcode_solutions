class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        needed_freq = {}
        count = 0
        for i in hours:
            key = i % 24
            if key in needed_freq:
                count += needed_freq[key]
                
            if key:
                key = 24 - key
            if key not in needed_freq:
                needed_freq[key] = 0
            needed_freq[key] += 1
        return count
        